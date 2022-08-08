FROM python:3.10.6-slim
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt
