import sqlite3
from persistence.database import connect_to_db, hash_password

def register(username, password, email, address, role):
    conn = connect_to_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password, email, address, role) VALUES (?, ?, ?, ?, ?)", (username, hash_password(password), email, address, role))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        print("User already exists")
        conn.close()
        return False

def login(email, password):
    conn = connect_to_db()
    cur = conn.cursor()
    hashed_pwd = hash_password(password)
    cur.execute("SELECT id, username, role FROM users WHERE email=? AND password=?",
                   (email, hashed_pwd))
    user = cur.fetchone()
    conn.close()
    if user is None:
        return False
    return {"id": user[0], "name": user[1], "role": user[2]}
