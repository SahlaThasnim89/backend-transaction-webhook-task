from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Transaction

router = APIRouter()


@router.get("/v1/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    db = SessionLocal()
    try:
        tx = (
            db.query(Transaction)
            .filter(Transaction.transaction_id == transaction_id)
            .first()
        )

        if not tx:
            raise HTTPException(status_code=404, detail="Not found")

        return tx

    finally:
        db.close()


