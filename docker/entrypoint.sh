#!/bin/sh
set -e

export PYTHONPATH=/tehnodel_backend:$PYTHONPATH
cd /tehnodel_backend

# ждем Postgres
echo "Waiting for Postgres at ${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432}..."
until nc -z "${POSTGRES_HOST:-db}" "${POSTGRES_PORT:-5432}"; do
  sleep 1
done

# гарантируем каталоги (на named volumes это уже есть, но лишним не будет)
mkdir -p back_static back_media || true

# миграции + статика
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# запускаем то, что пришло в CMD (gunicorn)
echo "Starting: $*"
exec "$@"
