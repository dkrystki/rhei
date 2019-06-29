FROM python:3.7

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV SHELL /bin/bash


# Install common
RUN apt update && pip3 install pipenv

# Setup motd
COPY docker/motd/motd /etc/motd
COPY docker/motd/.bashrc /root/.bashrc

# uid is set to 1000 for development purposes
RUN useradd -ms /bin/bash -u 1000 rhei
COPY docker/motd/.bashrc /home/rhei/.bashrc

RUN chown -R rhei:rhei /srv
WORKDIR /srv

COPY --chown=rhei:rhei . .
USER rhei

# PipEnv
ENV PIPENV_VENV_IN_PROJECT true
RUN pipenv install -d
RUN pipenv run python setup.py clean
