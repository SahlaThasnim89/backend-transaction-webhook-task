from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status":"HEALTHY",
        "current_time": datetime.utcnow()
        }

