FROM python:3.9

RUN pip install boto3

WORKDIR /app

COPY criacao-bucket.py .

CMD [ "python", "./criacao-bucket.py"]

