"""
This file contains the database initialization code.
"""

import sqlite3

DB_NAME = "food_delivery_app.db"

def connect_to_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn = connect_to_db()
    cur = conn.cursor()

    # cur.execute("DROP TABLE IF EXISTS users")
    # cur.execute("DROP TABLE IF EXISTS restaurants")
    # cur.execute("DROP TABLE IF EXISTS orders")

    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE delivery_agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            status INTEGER CHECK(status IN (0,1)) DEFAULT 1
        )
    """)

    cur.execute("""
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            item TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT CHECK(status IN ('pending', 'preparing', 'out_for_delivery', 'delivered')) DEFAULT 'pending',
            delivery_agent_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(assigned_agent) REFERENCES restaurants(id)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
