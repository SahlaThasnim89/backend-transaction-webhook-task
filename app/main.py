from fastapi import FastAPI
from app.database import engine, Base
from app.routes import health, webhooks, transactions

app = FastAPI()


app.include_router(health.router)
app.include_router(webhooks.router)
app.include_router(transactions.router)
