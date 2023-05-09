from fastapi import Depends

from .repository import PaymentRepository
from ...db import get_db_conn


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


class PaymentServiceTwo:
    def __init__(self, ):
        # setting this up even though we may not need it anywhere we get to
        pass
    def get_payments(self, payment_repository=Depends(PaymentRepository)):
        return payment_repository.get_payments()

    def test_payments_endpoint(self):
        _, cursor = self.db
        # this shows we are setting up a connection even though we don't need one for this
        # function
        return str(type(cursor))
