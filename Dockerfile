FROM python:3.11-slim-buster

MAINTAINER Ralf Junghanns <ralf.junghanns@tu-dresden.de>

COPY . /app
WORKDIR /app

# Install the requirements
RUN pip install -r ./requirements.txt
