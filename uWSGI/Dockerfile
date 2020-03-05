FROM python:3.7

RUN pip3 install uwsgi
COPY test.py /home/

WORKDIR /home/

ENTRYPOINT uwsgi --http :8000 --wsgi-file test.py

