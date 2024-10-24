from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',
        database='flask_db',
        user='flask_user',
        password='flask_password'
    )
    return conn

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    create_table()
    return jsonify(message="Welcome to Flask with PostgreSQL")

# curl --header "Content-Type: application/json" \
# --request POST \
# --data '{"name":"Lera"}' \
# http://127.0.0.1:8080/add

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

if __name__ == '__main__':
    # create_table()
    app.run(host='0.0.0.0', port=8080)
