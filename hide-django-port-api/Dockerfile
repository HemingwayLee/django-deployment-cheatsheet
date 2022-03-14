FROM python:3.7

RUN apt-get update && apt-get install -y \
  nginx \
  vim

RUN pip3 install django

COPY default /etc/nginx/sites-enabled/default 

COPY . /home
WORKDIR /home/webapp
RUN python3 manage.py migrate


ENTRYPOINT nginx && python3 manage.py runserver 0.0.0.0:8000  && /bin/bash

