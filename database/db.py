import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = os.path.join(BASE_DIR, "travel.db")


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()

    schema_path = os.path.join(BASE_DIR, "database", "schema.sql")

    with open(schema_path, "r", encoding="utf-8") as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()