#! /usr/bin/env bash

# Let the DB start
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"
do
  echo "Waiting for postgres at: $DB_HOST:$DB_PORT"
  sleep 2;
done

# Run migrations
alembic upgrade head

