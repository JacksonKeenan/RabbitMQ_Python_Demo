FROM python:3.8-slim-buster as build

WORKDIR /src

RUN pip3 install pika

COPY send.py /src

CMD [ "python3", "-u", "send.py" ]