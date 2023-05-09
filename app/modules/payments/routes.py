# fastapi router
from fastapi import APIRouter, Depends
from app.db import get_db_conn

from app.modules.payments.service import PaymentService, PaymentServiceTwo
from app.modules.payments.utils import payment_service as payment_service_util

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("")
def get_payments(payment_service: PaymentService = Depends(payment_service_util)):
    payments = payment_service.get_payments()
    return {"payments": payments}


@router.get("/payments2")
def get_payments(payment_service: PaymentService = Depends(PaymentServiceTwo)):
    payments = payment_service.get_payments()
    return {"payments": payments}

@router.get("/test")
def get_payments_test(db=Depends(get_db_conn)):
    resp = PaymentService(db).test_payments_endpoint()
    return {"resp": resp}


@router.post("")
async def create_payment(amount, confirmation_number, user_id):
    # call the function directly
    conn, cursor = get_db_conn()
    sql = f"INSERT INTO payments (amount, confirmation_number, user_id) VALUES ({amount}, {confirmation_number}, {user_id})"
    cursor.execute(sql)
    conn.commit()
