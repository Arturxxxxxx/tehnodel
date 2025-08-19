# ===== base =====
FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH="/home/appuser/.local/bin:${PATH}"
WORKDIR /app

# системные зависимости (psycopg / pillow и т.п.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# создаём непривилегированного пользователя
RUN useradd -ms /bin/bash appuser

# ===== deps =====
FROM base AS deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# ===== runtime =====
FROM base AS runtime
# копируем только установленные зависимости
COPY --from=deps /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=deps /usr/local/bin /usr/local/bin

# копируем проект
COPY . /app
# права
RUN chown -R appuser:appuser /app
USER appuser

# Скрипт запуска
COPY ./docker/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# gunicorn слушает на 8000
EXPOSE 8000

# по умолчанию – gunicorn (prod)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60"]
