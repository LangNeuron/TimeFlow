#!/bin/bash

CONTAINER_NAME="timeflow-db"

if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    echo "Container $CONTAINER_NAME exists. Removing..."
    docker rm -f $CONTAINER_NAME
fi

docker run -d \
  --name $CONTAINER_NAME \
  -e POSTGRES_USER=timeflow_user \
  -e POSTGRES_PASSWORD=secretpassword \
  -e POSTGRES_DB=timeflow_db \
  -p 5432:5432 \
  postgres:16

until docker exec $CONTAINER_NAME pg_isready -U timeflow_user; do
  echo "Waiting for Postgres..."
  sleep 2
done

echo "Running database migrations..."
poetry run alembic upgrade head


echo "Postgres is ready. Starting server..."
poetry run python src/start_server.py --dev
