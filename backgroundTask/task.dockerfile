FROM python:3.7

RUN apt-get update && apt-get -y install postgresql vim curl

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

RUN useradd -ms /bin/bash pyuser
USER pyuser

CMD bash init.sh

