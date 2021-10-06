# syntax=docker/dockerfile:1

# Use slim buster images
FROM python:3.8.5-slim-buster

# Make a working directory
RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# Copy the source code
ADD openforms /app

# Turn of debugging in production
ENV FLASK_DEBUG 0
ENV FLASK_APP openforms
ENV FLASK_ENV development

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]

LABEL maintainer="Rahul Palve <hi.rahulpalve@gmail.com>"
# ADD: wsgi and nginx