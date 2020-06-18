#!/bin/bash

until PGPASSWORD=${DBPASS} psql -h ${DBHOST} -p 5432 -U ${DBUSER} -d ${DBNAME} -c "\q"; do
  >&2 echo "Postgres is not available, sleep..."
  sleep 1
done

>&2 echo "Postgres is up"

python3 manage.py makemigrations
python3 manage.py migrate


USER="root"
PASS="rootroot"
MAIL="root@gmail.com"
SCRIPT="
from django.contrib.auth.models import User
username = '$USER'
password = '$PASS'
email = '$MAIL'
if User.objects.filter(username=username).count()==0:
  User.objects.create_superuser(username, email, password)
  print('Super user created!')
else:
  print('Skip! super user exists...')
"

printf "$SCRIPT" | python3 manage.py shell
python3 manage.py runserver 0.0.0.0:8000


