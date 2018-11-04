FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  python3-venv 

RUN pip3 install uwsgi
COPY test.py /home/

WORKDIR /home/

ENTRYPOINT uwsgi --http :8000 --wsgi-file test.py && /bin/bash


