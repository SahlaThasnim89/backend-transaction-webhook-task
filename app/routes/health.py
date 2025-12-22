from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
def health():
    return {
        "status":"HEALTHY",
        "current_time": datetime.utcnow()
        }

