import sqlite3
import pathlib



# @magic_bind_to_container(container)
def get_db_conn():
    root_path = pathlib.Path(__file__).parent

    db = f"{root_path}/database.sqlite"

    conn = sqlite3.connect(db)
    return conn, conn.cursor()


class SqlLiteConnection:
    def __init__(self):
        root_path = pathlib.Path(__file__).parent

        db = f"{root_path}/database.sqlite"

        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
