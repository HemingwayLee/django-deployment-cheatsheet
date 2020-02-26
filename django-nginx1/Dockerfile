FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  python3-venv \
  nginx \
  vim

RUN pip3 install django

COPY default /etc/nginx/sites-enabled/default

WORKDIR /home
RUN django-admin startproject mysite

WORKDIR /home/mysite
RUN python3 manage.py migrate

ENTRYPOINT nginx && python3 manage.py runserver 0.0.0.0:8000  && /bin/bash


