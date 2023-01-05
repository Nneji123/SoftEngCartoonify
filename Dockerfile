FROM python:3.8.13-slim-bullseye

WORKDIR /app

RUN apt-get -y update && apt-get install -y \
  wget \
  ffmpeg \ 
  libsm6 \
  libxext6

RUN pip install --upgrade setuptools 

COPY . .

RUN pip install -r requirements.txt


# RUN python init_db

CMD python backend/app.py