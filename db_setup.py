import sqlite3
from flask import g


DATABASE = 'S:\\PROJECTS\\FLASK_projects\\membership_system_restfull_api_flask\\members.db'


def get_db():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
    return conn


# CREATE
def insert_db(query, args=()):
    conn = get_db()
    cursor = conn.execute(query, args)
    conn.commit()
    cursor.close()


# READ
def query_db(query, args=(), one=False):
    conn = get_db()
    cursor = conn.execute(query, args)
    data = cursor.fetchall()
    cursor.close()
    return (data[0] if data else None) if one else data


# UPDATE
def update_db(query, args=()):
    conn = get_db()
    cursor = conn.execute(query, args)
    conn.commit()
    cursor.close()


# DELETE
def delete_db(query, args=()):
    conn = get_db()
    cursor = conn.execute(query, args)
    conn.commit()
    cursor.close()
