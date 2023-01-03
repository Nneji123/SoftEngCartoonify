FROM python:3.8.13-slim-bullseye

WORKDIR /app

RUN apt-get -y update && apt-get install -y \
  wget \
  ffmpeg \ 
  libsm6 \
  libxext6

RUN pip install --upgrade setuptools 

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD . . 


# RUN python init_db
ARG POSTGRES="postgresql://postgres:nbnvTZvJEYEZnnSUKoHy@containers-us-west-114.railway.app:7101/railway"
ARG SQLITE="sqlite:///../database.db"
ARG SECRET_KEY="secret_key"
ARG DATABASE_MODE="postgres"

# RUN python init_db.py

CMD python backend/app.py