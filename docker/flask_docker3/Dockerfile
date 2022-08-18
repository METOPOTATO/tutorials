FROM python:3.9.0

WORKDIR /myapp

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# docker build --tag myflaskdocker .
# docker run 