#!/bin/bash
set -e

echo "Waiting for PostgreSQL..."
until pg_isready -h db -p 5432 -U postgres; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Running migrations..."
alembic upgrade head

echo "Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
