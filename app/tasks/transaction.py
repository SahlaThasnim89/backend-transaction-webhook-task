import time
from datetime import datetime

from app.tasks.celery_app import celery
from app.database import SessionLocal
from app.models.transaction import Transaction



@celery.task(bind=True, autoretry_for=(Exception,),retry_backoff=5, retry_kwargs={"max_retries": 3})
def process_transaction(self, transaction_id: str):

    db = SessionLocal()
    try:
        txn = (
            db.query(Transaction)
            .filter_by(transaction_id=transaction_id)
            .one()
        )

        txn.status = "PROCESSING"
        db.commit()

        # Simulate external API / bank processing
        time.sleep(30)

        txn.status = "PROCESSED"
        txn.processed_at = datetime.utcnow()
        db.commit()

    finally:
        db.close()
