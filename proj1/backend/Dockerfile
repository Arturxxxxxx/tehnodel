FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /tehnodel_backend

# системные либы для psycopg2, Pillow и т.п.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev netcat-openbsd \
    libjpeg62-turbo-dev zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# код проекта
COPY . .

# entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# подготовим каталоги статики/медиа (будут заменены томами, но на чистом образе полезно)
RUN mkdir -p /tehnodel_backend/back_static /tehnodel_backend/back_media

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn","config.wsgi:application","--bind","0.0.0.0:8000","--workers","4","--threads","2","--timeout","60"]
