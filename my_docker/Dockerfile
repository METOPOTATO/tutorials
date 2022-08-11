FROM python:3.9.6

WORKDIR /app/

RUN apt-get update && apt-get -y install gdal-bin libgdal-dev

COPY ./api/requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./api .

EXPOSE 8989

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0:8989"]