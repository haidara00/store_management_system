FROM python:3.11


WORKDIR /code

COPY Pipfile Pipfile.lock /code/


RUN pip install pipenv && pipenv install --system

COPY . /code/
