from celery import Celery
from time import sleep
from datetime import datetime

from app.config import REDIS_URL
from app.database import SessionLocal
from app.models import Transaction

celery = Celery("worker", broker=REDIS_URL)


@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=5)
def process_transaction(self, transaction_id: str):
    # simulate external processing delay
    sleep(30)

    db = SessionLocal()
    try:
        tx = (
            db.query(Transaction)
            .filter(Transaction.transaction_id == transaction_id)
            .first()
        )

        # idempotency check
        if not tx or tx.status == "PROCESSED":
            return

        tx.status = "PROCESSED"
        tx.processed_at = datetime.utcnow()

        db.commit()

    finally:
        db.close()
