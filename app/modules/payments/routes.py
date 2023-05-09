# fastapi router
from fastapi import APIRouter
from app.db import get_db_conn

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("")
def get_payments():
    # call the function directly
    _, cursor = get_db_conn()
    cursor.execute("SELECT * FROM payments")
    payments = cursor.fetchall()
    return {"payments": payments}


@router.post("")
async def create_payment(amount, confirmation_number, user_id):
    # call the function directly
    conn, cursor = get_db_conn()
    sql = f"INSERT INTO payments (amount, confirmation_number, user_id) VALUES ({amount}, {confirmation_number}, {user_id})"
    cursor.execute(sql)
    conn.commit()