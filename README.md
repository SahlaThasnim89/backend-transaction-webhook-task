Transaction Webhook Processor

A production-style backend service built with FastAPI, PostgreSQL, Celery, and Redis that receives transaction webhooks and processes them asynchronously.

Architecture Overview

Components

FastAPI – Receives webhooks and exposes query endpoints

PostgreSQL – Persists transaction state

Celery + Redis – Asynchronous background processing

Alembic – Database schema migrations

Docker Compose – Local orchestration

Processing Flow

Webhook received → transaction stored with status PENDING

Celery task enqueued

Background task simulates processing (30s delay)

Transaction updated to PROCESSED

Tech Stack

Python 3.11
FastAPI
SQLAlchemy
Alembic
PostgreSQL
Celery
Redis
Docker & Docker Compose

#Prerequisites:-

Docker

Docker Compose

No local Python or database installation required.

Running the Service

1. Build and start containers

docker compose up --build -d


This starts:

API service

PostgreSQL database

Redis

Celery worker

Database Migrations (IMPORTANT)

This project uses Alembic for schema management.

First-Time Setup (Required)

When running the project for the first time, database tables must be created:

docker compose exec api alembic upgrade head


This command:

Creates all required tables (e.g. transactions)

Initializes Alembic version tracking

⚠️ This step is required only once per fresh database.

Normal Runs

After migrations are applied, you can simply run:

docker compose up


No additional setup is required.

Regenerating Migrations (Developer Use)

If you modify SQLAlchemy models:

docker compose exec api alembic revision --autogenerate -m "describe change"
docker compose exec api alembic upgrade head

API Usage
Webhook Endpoint

POST /webhook

Example request:

curl -X POST http://localhost:8000/webhook \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_id": "txn_001",
    "source_account": "A123",
    "destination_account": "B456",
    "amount": 100,
    "currency": "USD"
  }'


Expected Behavior

Immediately saved as PENDING

Updated to PROCESSED after ~30 seconds by background worker

Transaction States

PENDING – Received and queued

PROCESSED – Successfully processed

Design Considerations

Asynchronous processing using Celery to keep API responsive

Idempotent transaction handling

Retry-safe background jobs

Clear separation of concerns:

API layer

Database layer

Background workers

Production-like setup using Docker Compose

Notes for Evaluators

Database schema is versioned using Alembic

Background processing is intentionally delayed to demonstrate async execution

Dockerized setup ensures easy reproducibility

Clean module separation avoids circular dependencies

Stopping the Service
docker compose down


To reset everything (including database):

docker compose down -v

Author

Sahla Thasnim
