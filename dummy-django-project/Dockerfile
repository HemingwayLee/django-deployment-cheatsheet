FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  python3-venv \
  tree

RUN pip3 install django

WORKDIR /home
RUN django-admin startproject mysite

WORKDIR /home/mysite
RUN python3 manage.py migrate
RUN tree .

ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000 && /bin/bash

