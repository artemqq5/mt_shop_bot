#!/bin/bash
set -e

echo "🔁 Running Alembic migrations..."
alembic upgrade head

echo "🚀 Starting bot..."
exec python -m uvicorn bot.main:app --host 0.0.0.0 --port 8006
