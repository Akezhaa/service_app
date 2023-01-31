FROM --platform=linux/amd64 python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN addgroup -S servgroup

RUN adduser -S -D -h /service service-user servgroup

RUN chown -R service-user:servgroup /service

USER service-user