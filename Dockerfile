FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11 AS backend-base
FROM node:18 AS frontend-base

# Backend
FROM backend-base AS backend-dev
WORKDIR /app

ENV DB_HOST=postgres
ENV DB_USER=postgres
ENV DB_PASS=postgres
ENV DB_NAME=postgres
ENV DB_PORT=5432
ENV LOG_LEVEL=info

RUN apt-get update && apt-get install -y postgresql-client
COPY ./prestart.sh /app/prestart.sh
COPY ./start-reload.sh /start-reload.sh
COPY ./start.sh /start.sh
RUN chmod +x /app/prestart.sh /start-reload.sh /start.sh

COPY ./requirements.txt /app/requirements.txt
COPY ./alembic.ini /app/alembic.ini

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY app/ /app/app
COPY migrations/ /app/migrations

EXPOSE 80

ENTRYPOINT ["/start-reload.sh"]

# Frontend
FROM frontend-base AS frontend-dev
WORKDIR /src
COPY frontend/ /src
RUN npm install
ENTRYPOINT ["bash", "-c", "npm install && npm run serve"]

# Frontend Build
FROM frontend-dev AS frontend-build
RUN npm run build

# Combined Prod
FROM backend-dev AS backend-prod
COPY --from=frontend-build /src/dist /app/static

RUN chown -Rf www-data:www-data /app

USER www-data

ENTRYPOINT ["/start.sh"]
