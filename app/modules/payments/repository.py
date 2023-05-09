# this is the class for database layer abstraction
from fastapi import Depends

from app.db import get_db_conn


class PaymentRepository:

    def __init__(self, db = get_db_conn):
        self.db = db()

    def get_payments(self):
        _, cursor = self.db
        cursor.execute("SELECT * FROM payments")
        payments = cursor.fetchall()
        return payments