FROM python:3.7

RUN apt-get update && apt-get install -y \
  nginx \
  vim \
  gettext-base

ENV MY_IP 127.0.0.1
ENV MY_PORT 8000
RUN pip3 install django

COPY nginx.conf.template /home/nginx.conf.template
COPY run_nginx.sh /home/run_nginx.sh
RUN /home/run_nginx.sh

WORKDIR /home
RUN django-admin startproject mysite

WORKDIR /home/mysite
RUN python3 manage.py migrate

COPY settings.py /home/mysite/mysite

ENTRYPOINT nginx && python3 manage.py runserver 0.0.0.0:8000  && /bin/bash
