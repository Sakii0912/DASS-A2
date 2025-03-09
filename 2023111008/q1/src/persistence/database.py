"""
This file contains the database initialization code.
"""

import sqlite3
import hashlib

DB_NAME = "food_delivery_app.db"

def connect_to_db():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            role TEXT CHECK(role IN ('customer', 'manager')) NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS delivery_agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            status INTEGER CHECK(status IN (0,1)) DEFAULT 1
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            item_id TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            status TEXT CHECK(status IN ('pending', 'preparing', 'out_for_delivery', 'delivered')) DEFAULT 'pending',
            FOREIGN KEY(user_id) REFERENCES users(id)
            FOREIGN KEY(item_id) REFERENCES menu(id)
        )
    """)

    conn.commit()
    conn.close()

def menu():
    conn = connect_to_db()
    cur = conn.cursor()

    sample_menu = [
        ("Burger", 5.99),
        ("Pizza", 8.99),
        ("Pasta", 7.49),
        ("Salad", 4.99),
        ("Soda", 1.99)
    ]

    cur.executemany("INSERT INTO menu (name, price) VALUES (?, ?)", sample_menu)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    menu()
