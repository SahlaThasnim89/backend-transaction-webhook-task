from fastapi import APIRouter, status
from sqlalchemy.exc import IntegrityError

from app.schemas import TransactionIn
from app.database import SessionLocal
from app.models import Transaction
from app.tasks import process_transaction

router = APIRouter()


@router.post("/v1/webhooks/transactions", status_code=status.HTTP_202_ACCEPTED)
def receive_webhook(payload: TransactionIn):
    db = SessionLocal()

    try:
        tx = Transaction(**payload.dict(), status="PROCESSING")
        db.add(tx)
        db.commit()

        # fire-and-forget background task
        process_transaction.delay(payload.transaction_id)

    except IntegrityError:
        # duplicate webhook → safely ignore
        db.rollback()

    finally:
        db.close()

    return {"ack": "accepted"}


