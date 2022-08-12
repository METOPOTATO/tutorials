FROM python:3.8-slim-buster

WORKDIR /flask

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]

