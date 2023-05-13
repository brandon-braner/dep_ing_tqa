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


def _auto_close_db_connection():
    # this is a helper function to close the connection when the request is done
    # this is a helper function to close the connection when the request is done
    def _close_db_connection():
        conn, _ = get_db_conn()
        conn.close()

    return _close_db_connection