FROM python:3.10.2

RUN pip install pipenv

ADD . /produtitas

WORKDIR /produtitas
