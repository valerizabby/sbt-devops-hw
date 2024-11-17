import pytest
from app.app import app, create_table

CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    '''

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    """Тест главной страницы."""

    def mock_create_table():
        pass

    monkeypatch.setattr('app.app.create_table', mock_create_table)
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to Flask with PostgreSQL"}


def test_add_item(client, monkeypatch):
    """Тест добавления элемента."""

    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query, params=None):
                pass

            def close(self):
                pass

        class MockConn:
            def cursor(self):
                return MockCursor()

            def commit(self):
                pass

            def close(self):
                pass

        return MockConn()

    monkeypatch.setattr('app.app.get_db_connection', mock_get_db_connection)

    response = client.post('/add', json={'name': 'Test Item'})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Item added successfully"}



def test_create_table(monkeypatch):
    """Тест функции create_table."""

    # Мокаем соединение с базой данных
    def mock_get_db_connection():
        class MockCursor:
            def execute(self, query):
                # Проверяем, что запрос на создание таблицы корректен
                assert query == CREATE_TABLE

            def close(self):
                pass

        class MockConn:
            def cursor(self):
                return MockCursor()

            def commit(self):
                pass

            def close(self):
                pass

        return MockConn()

    # Заменяем реальную функцию get_db_connection на мок
    monkeypatch.setattr('app.app.get_db_connection', mock_get_db_connection)

    # Вызываем функцию create_table
    create_table()


def test_jenkins_endpoint(client):
    """Тест эндпоинта /jenkins"""
    response = client.get('/jenkins')
    assert response.status_code == 200
    assert response.get_json() == {"message": "I'm visible from Jenkins!"}