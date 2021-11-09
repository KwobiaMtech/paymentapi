# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/paymentapi

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apt-get install tzdata

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh","/usr/src/paymentapi/entrypoint.sh"]