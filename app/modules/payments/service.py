from .repository import PaymentRepository


class PaymentService:
    def __init__(self, db):
        self.db = db
        # setting this up even though we may not need it anywhere we get to
        self.payment_repository = PaymentRepository(self.db)

    def get_payments(self):
        return self.payment_repository.get_payments()

    def test_payments_endpoint(self):
        _, cursor = self.db
        # this shows we are setting up a connection even though we don't need one for this
        # function
        return str(type(cursor))