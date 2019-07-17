FROM python:3.7-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV SHELL /bin/bash


RUN pip3 install pipenv

WORKDIR /srv
COPY . .

# PipEnv
RUN pipenv install -d --system


COPY docker/motd/motd /etc/motd

# Fix user owwnership
RUN addgroup --gid 1000 rhei && adduser --disabled-password --disabled-login --gecos "" --uid 1000 --gid 1000 rhei

USER rhei

# uncomment aliases and colors
RUN echo "force_color_prompt=yes" /home/rhei/.bashrc
RUN echo "alias ll='ls -l'" >> /home/rhei/.bashrc
RUN echo "alias la='ls -A'" >> /home/rhei/.bashrc

# Setup motd
COPY docker/motd/motd /etc/motd
RUN echo "echo -e \"`cat /etc/motd`\"" >> /home/rhei/.bashrc
