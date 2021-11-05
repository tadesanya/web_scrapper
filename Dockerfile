FROM python:3.7-alpine3.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /web_scraper

# set work directory
WORKDIR /web_scraper

# Copy and install requirements
RUN pip install --upgrade pip
COPY requirements.txt /web_scraper/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /store_app
COPY . /web_scraper/

EXPOSE 8000