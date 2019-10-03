FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add --virtual python-dev3 && \
    apk add mysql-client && \
    apk add gcc && \
    apk add libc-dev && \
    apk add linux-headers && \
    apk add mariadb-dev
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./ /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
