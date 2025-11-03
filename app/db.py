import sqlite3
from bcrypt import checkpw, hashpw, gensalt
from config import DB_FILE

def get_connection():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def create_user(username, password):
    conn = get_connection()
    try:
        hashed = hashpw(password.encode(), gensalt()).decode()
        conn.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = get_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    if user:
        return checkpw(password.encode(), user["hashed_password"].encode())
    return False

def get_user_id(username):
    conn = get_connection()
    user = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return user["id"] if user else None

def save_chat(user_id, query, response):
    conn = get_connection()
    conn.execute(
        "INSERT INTO chat_history (user_id, query, response) VALUES (?, ?, ?)",
        (user_id, query, response)
    )
    conn.commit()
    conn.close()

def get_chats(user_id, limit=8):
    conn = get_connection()
    chats = conn.execute(
        "SELECT id, query, timestamp FROM chat_history WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?",
        (user_id, limit)
    ).fetchall()
    conn.close()
    return chats
