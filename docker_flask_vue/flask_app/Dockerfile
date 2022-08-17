FROM python:3.9.6

WORKDIR /flask_app

RUN apt-get update && apt-get -y install python3-pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

# CMD ["python3", "app.py"]
