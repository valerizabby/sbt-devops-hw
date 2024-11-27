from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    '''

def get_db_connection():
    conn = psycopg2.connect(
        host='flask_db',
        database='flask_db',
        user='flask_user',
        password='flask_password'
    )
    return conn

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(CREATE_TABLE)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    create_table()
    return jsonify(message="Welcome to Flask with PostgreSQL")


@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    name = data.get('name')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name) VALUES (%s)', (name,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify(message="Item added successfully")

@app.route('/jenkins')
def jenkins_endpoint():
    return jsonify(message="I'm visible from Jenkins!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

def main():
    app.run(host='0.0.0.0', port=5555)