from fastapi import APIRouter, status, Response, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import IntegrityError


from app.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionIn
from app.tasks.transaction import process_transaction

router = APIRouter()


@router.post("/v1/webhooks/transactions", status_code=status.HTTP_202_ACCEPTED)
def handle_transaction_webhook(
    payload: TransactionIn,
    db: Session = Depends(get_db)
):
    try:
        txn = Transaction(
            transaction_id=payload.transaction_id,
            source_account=payload.source_account,
            destination_account=payload.destination_account,
            amount=payload.amount,
            currency=payload.currency,
            status="PENDING",
            created_at=datetime.utcnow(),
            processed_at=None
        )
        db.add(txn)
        db.commit()

        process_transaction.delay(payload.transaction_id)

    except IntegrityError:
        db.rollback()
        return {"ack": "duplicate ignored"}

    return {"ack": "accepted"}



