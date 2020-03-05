FROM python:3.7

RUN apt-get update && apt-get install -y nginx vim

RUN pip3 install uwsgi
RUN pip3 install django

COPY default /etc/nginx/sites-enabled/default

WORKDIR /home
RUN django-admin startproject mysite

WORKDIR /home/mysite
RUN python3 manage.py migrate
RUN cp /etc/nginx/uwsgi_params /home/mysite

ENTRYPOINT nginx && uwsgi --socket :8001 --module mysite.wsgi

# uWSGI will run in the foreground, no need to add `/bin/bash`
# ENTRYPOINT nginx && uwsgi --socket :8001 --module mysite.wsgi && /bin/bash


