# this is the class for database layer abstraction
class PaymentRepository:

    def __init__(self, db):
        self.db = db

    def get_payments(self):
        _, cursor = self.db
        cursor.execute("SELECT * FROM payments")
        payments = cursor.fetchall()
        return payments