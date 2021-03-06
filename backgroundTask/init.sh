#!/bin/bash

until PGPASSWORD=${DBPASS} psql -h ${DBHOST} -p 5432 -U ${DBUSER} -d ${DBNAME} -c "\q"; do
  >&2 echo "Postgres is not available, sleep..."
  sleep 1
done

>&2 echo "Postgres is up"

until $(curl --output /dev/null --silent --head http://${BACKEND_IP}:${BACKEND_PORT}); do
  >&2 echo "backend is not available, sleep..."
  sleep 1
done

>&2 echo "backend server is up"

python3 src/runner.py

