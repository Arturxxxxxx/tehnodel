#!/usr/bin/env bash
set -e

# ждём БД (простая проверка)
if [ -n "${POSTGRES_HOST}" ]; then
  echo "Waiting for Postgres at ${POSTGRES_HOST}:${POSTGRES_PORT:-5432}..."
  until python - <<PY
import sys, socket, os
host=os.getenv("POSTGRES_HOST","db"); port=int(os.getenv("POSTGRES_PORT","5432"))
s=socket.socket(); s.settimeout(1)
try:
    s.connect((host,port)); s.close(); sys.exit(0)
except Exception as e:
    sys.exit(1)
PY
  do
    sleep 1
  done
fi

# миграции и сбор статики по желанию
python manage.py migrate --noinput

# Если есть статика — раскомментируй:
python manage.py collectstatic --noinput

# dev режим: DJANGO_DEV=1 -> runserver
if [ "${DJANGO_DEV}" = "1" ]; then
  echo "Running in DEV mode (runserver + autoreload)"
  exec python manage.py runserver 0.0.0.0:8000
fi

# иначе — стандартная команда (gunicorn из CMD)
exec "$@"
