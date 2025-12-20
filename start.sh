#!/bin/bash
set -e

# Port for API
PORT=${PORT:-8000}

# Postgres settings
DB_HOST=${PGHOST:-db}          # 'db' for local Docker, PGHOST from Render
DB_PORT=${PGPORT:-5432}        # 5432 default locally
DB_USER=${PGUSER:-postgres}
DB_PASSWORD=${PGPASSWORD:-postgres}
DB_NAME=${PGDATABASE:-appdb}

export PGPASSWORD="$DB_PASSWORD"  # required by pg_isready

echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Running migrations..."
alembic upgrade head

echo "Starting API on port $PORT..."
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT"

