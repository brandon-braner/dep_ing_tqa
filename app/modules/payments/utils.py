from app.modules.payments.service import PaymentService
from app.db import get_db_conn


def payment_service():
    db = get_db_conn()
    return PaymentService(db)
