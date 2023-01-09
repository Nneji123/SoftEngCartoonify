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

ENV POSTGRES postgresql://postgres:nbnvTZvJEYEZnnSUKoHy@containers-us-west-114.railway.app:7101/railway
ENV SQLITE sqlite:///../database.db
ENV SECRET_KEY secret_key 
ENV DATABASE_MODE sqlite
ENV PORT 5000
ENV GOOGLE_CLIENT_ID value
ENV GOOGLE_CLIENT_SECRET value
ENV GOOGLE_DISCOVERY_URL value
ENV DEBUG value

RUN python init_db.py

CMD gunicorn app:app