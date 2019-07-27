
====================================
Rhei - Simple stopwatch class
====================================

.. image:: https://badge.fury.io/py/rhei.svg
    :target: https://pypi.org/project/rhei/

.. image:: https://circleci.com/gh/dkrystki/rhei.svg?style=svg
    :target: https://circleci.com/gh/dkrystki/rhei

.. image:: https://codecov.io/gh/dkrystki/rhei/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dkrystki/rhei

.. image:: https://img.shields.io/badge/python-3.6-blue.svg
    :target: https://www.python.org/downloads/release/python-360/

.. image:: https://img.shields.io/badge/python-3.7-blue.svg
    :target: https://www.python.org/downloads/release/python-370/


Rhei is a Python 3 package that implements simple stopwatch functionality including pausing, resetting and reverse counting.

Installation
------------
.. code-block:: console

    pip install rhei


In a nutshell
-------------

.. code-block:: python

    from time import sleep
    from rhei import Stopwatch

    stopwatch = Stopwatch()
    stopwatch.start()
    sleep(5)
    stopwatch.value  # 5.0

    stopwatch.pause()
    sleep(2)
    stopwatch.value  # 5.0

    stopwatch.reset()
    stopwatch.value  # 0.0

    stopwatch.reset(10.0)
    stopwatch.value  # 10.0
    stopwatch.start(reversed=True)  # Start counting down

    sleep(2)
    stopwatch.value  # -2.0

Development
-----------
Rhei uses docker to create an isolated development environment so your system is not being polluted.

Requirements
############
In order to run local development you have to have Docker and Docker Compose installed.


Starting things up
##################
.. code-block:: console

    docker-compose up -d

Logging into the docker terminal
################################
.. code-block:: console

    ./bin/host/terminal

The code is synchronised between a docker container and the host using volumes so any changes ( ``pipenv install`` etc ) will be affected on the host.
