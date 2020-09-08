import sqlite3

DBPATH = "../database.db"


def get_db_connection():

    with sqlite3.connect(DBPATH) as conn:
        return conn
