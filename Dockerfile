# syntax=docker/dockerfile:1

# Use slim buster images
FROM python:3.8.5-slim-buster

# Make a working directory
RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# Copy the source code
ADD openforms /app/openforms
COPY ./wsgi.py /app

# Turn of debugging in production
ENV FLASK_DEBUG 1
ENV FLASK_ENV development

ENTRYPOINT ["python", "-m", "gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "wsgi:app"]

LABEL maintainer="Rahul Palve <hi.rahulpalve@gmail.com>"
# ADD: wsgi and nginx
