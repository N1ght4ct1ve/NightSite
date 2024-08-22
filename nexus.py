import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = 'nexus.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def create_user(username, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    hashed_password = generate_password_hash(password)
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT id, username FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def add_file(filename, user_id):
    # Implementiere hier die Logik für das Speichern von Dateien, falls notwendig
    pass

def get_files_by_user_id(user_id):
    # Implementiere hier die Logik für das Abrufen von Dateien, falls notwendig
    return []

if __name__ == "__main__":
    init_db()