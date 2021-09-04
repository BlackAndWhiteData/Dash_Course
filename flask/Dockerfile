FROM python:3.9.7-buster

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip

RUN pip install -r requirements_minimal.txt

CMD ["uwsgi", "app.ini"] 
