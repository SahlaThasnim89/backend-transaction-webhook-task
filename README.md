# Transaction Webhook Processor

A production-style backend service built with FastAPI, PostgreSQL, Celery, and Redis that receives transaction webhooks and processes them asynchronously.

# Overview

This service demonstrates a real-world backend architecture for handling incoming webhooks and processing them in the background without blocking API responses.

# Architecture-Components

FastAPI – Receives webhooks and exposes API endpoints

PostgreSQL – Persists transaction data and state

Celery + Redis – Handles asynchronous background processing

Alembic – Manages database schema migrations

Docker Compose – Orchestrates all services locally

# Processing Flow

Webhook received → transaction stored with status PENDING

Celery task is enqueued

Background worker simulates processing (30-second delay)

Transaction status updated to PROCESSED

# Tech Stack

Python 3.11

FastAPI

SQLAlchemy

Alembic

PostgreSQL

Celery

Redis

Docker & Docker Compose

Prerequisites

Docker

Docker Compose

=======
No local Python or database installation is required.

# Getting Started
Build and Start Services
```docker compose up --build -d```

This starts:
API service

=======
PostgreSQL database
Redis
Celery worker
Database Migrations
This project uses Alembic for database schema management.

First-Time Setup (Required)

# On the first run, database tables must be created:
```docker compose exec api alembic upgrade head```


This will:

Create all required tables (e.g. transactions)

Initialize Alembic version tracking

⚠️ This step is required only once per fresh database.

Normal Usage

After migrations are applied:
```docker compose up```
>>>>>>> 0ff0117e5dcf55bdad9f821c69d17771199c38ae


No additional setup is required.


# Regenerating Migrations (Development Only)

If SQLAlchemy models are updated:
```docker compose exec api alembic revision --autogenerate -m "describe change"```
```docker compose exec api alembic upgrade head```

# API Reference
>>>>>>> 0ff0117e5dcf55bdad9f821c69d17771199c38ae
Webhook Endpoint

POST /webhook

Example Request
curl -X POST http://localhost:8000/v1/webhooks/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_id": "txn_001",
    "source_account": "A123",
    "destination_account": "B456",
    "amount": 100,
    "currency": "USD"
  }'

Expected Behavior

Transaction is immediately saved with status PENDING

Status is updated to PROCESSED after ~30 seconds by the background worker

Transaction States
State	Description
PENDING	Webhook received and queued for processing
PROCESSED	Transaction successfully processed
Design Considerations

Non-blocking API using asynchronous background processing

Idempotent transaction handling

Retry-safe Celery tasks

Clear separation of concerns:

API layer

Database layer

Background workers

Dockerized setup for consistent and reproducible environments

Stopping the Service
```docker compose down```

Reset Everything (Including Database)
```docker compose down -v```

# Notes for Evaluators

Database schema is versioned using Alembic
Artificial delay demonstrates asynchronous execution
Docker Compose ensures easy local setup and reproducibility
Clean project structure avoids circular dependencies

Author
Sahla Thasnim
