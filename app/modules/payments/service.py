from fastapi import Depends

from .repository import PaymentRepository
from lagom import magic_bind_to_container

from ...container import container


class PaymentService:

    # def __init__(self, payment_repository: PaymentRepository):
    #     self.payment_repository = payment_repository


    @magic_bind_to_container(container)
    def get_payments(self, payment_repository: PaymentRepository):
        # bound to container so we only need to get the repository on endpoints that need it
        return payment_repository.get_payments()

    # def test_payments_endpoint(self):
    #     _, cursor = self.db
    #     # this shows we are setting up a connection even though we don't need one for this
    #     # function
    #     return str(type(cursor))
