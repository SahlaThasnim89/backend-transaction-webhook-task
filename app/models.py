from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    source_account = Column(String, nullable=False)
    destination_account = Column(String, nullable=False)

    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(3), nullable=False)

    status = Column(String, index=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    processed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
