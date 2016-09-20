FROM debian:jessie
MAINTAINER Dan LaMotte "lamotte85@gmail.com"

RUN \
    apt-get -qq update \
    && apt-get install -y python python-pip python-dev build-essential \
    && pip install Flask \
    && rm -fr /var/lib/apt/lists/*

WORKDIR /app
COPY app.py /app

CMD ["/usr/bin/python", "app.py"]
