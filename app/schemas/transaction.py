from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionIn(BaseModel):
    transaction_id:str
    source_account:str
    destination_account:str
    amount:float
    currency:str

class TransactionOut(TransactionIn):
    status:str
    created_at: datetime
    processed_at:Optional[datetime]

