# this is the class for database layer abstraction

from app.db import SqlLiteConnection


class PaymentRepository:

    def __init__(self, db: SqlLiteConnection):
        self.db = db

    def get_payments(self):
        self.db.cursor.execute("SELECT * FROM payments")
        payments = self.db.cursor.fetchall()
        return payments
