FROM python:3.9.5-alpine

RUN pip install gunicorn --upgrade pip

ADD . /customer-service-api
WORKDIR /customer-service-api

COPY . /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

EXPOSE 5002

CMD ["gunicorn", "--config=gunicorn.py", "run:app"]