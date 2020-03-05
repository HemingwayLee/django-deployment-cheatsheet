FROM python:3.7

RUN pip3 install uwsgi
RUN pip3 install django

WORKDIR /home
RUN django-admin startproject mysite

WORKDIR /home/mysite
RUN python3 manage.py migrate

ENTRYPOINT uwsgi --http :8000 --module mysite.wsgi

# uWSGI will run on the foreground, no need to add /bin/bash
# ENTRYPOINT uwsgi --http :8000 --module mysite.wsgi && /bin/bash

