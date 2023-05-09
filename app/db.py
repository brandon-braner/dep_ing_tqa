import sqlite3
import pathlib


def get_db_conn():
    root_path = pathlib.Path(__file__).parent

    db = f"{root_path}/database.sqlite"

    conn = sqlite3.connect(db)
    return conn, conn.cursor()

