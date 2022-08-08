FROM python:3.10.6-slim

WORKDIR /src
ADD requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

ADD . /src
