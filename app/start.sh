#!/bin/sh
set -e

alembic revision --autogenerate -m "new"

echo "Running migrations..."
alembic upgrade head

echo "Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}
