FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  python3-venv \
  tmux

RUN pip3 install django

WORKDIR /home
RUN django-admin startproject mysite

WORKDIR /home/mysite
RUN python3 manage.py migrate
# RUN tmux new-session -d -s "myDjangoSession" "python3 manage.py runserver 0.0.0.0:8000"

ENTRYPOINT ["/bin/bash"]


# docker build -t my-django .
# docker run -it -p 8000:8000 --rm my-django

