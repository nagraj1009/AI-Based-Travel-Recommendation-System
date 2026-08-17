import sqlite3

DATABASE = "travel.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():

    conn = get_connection()

    with open("database/schema.sql", "r") as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()