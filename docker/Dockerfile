FROM python:3.7-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV SHELL /bin/bash


RUN pip3 install pipenv

WORKDIR /srv
COPY . .

RUN bash ./docker/debug/setup.sh rhei

RUN pipenv install -d --system
