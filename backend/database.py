import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        face_encoding BLOB
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        vehicle TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()
