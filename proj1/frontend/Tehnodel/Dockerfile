# Сборка
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
# для Vite/CRA/Vue:
RUN npm run build

# Сервер статики
FROM nginx:1.27-alpine
# Vite/Vue обычно кладёт сборку в /app/dist; CRA — в /app/build
# если у тебя CRA — замени строку ниже на /app/build
COPY --from=builder /app/dist /usr/share/nginx/html

# SPA‑роутинг (index.html для любых путей)
RUN printf 'server { \
  listen 80; \
  server_name _; \
  root /usr/share/nginx/html; \
  index index.html; \
  location / { try_files $uri /index.html; } \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 80