FROM ubuntu:trusty
MAINTAINER lorin@ansiblebook.com

# Create self-signed cert for 192.168.56.11
ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y openssl

RUN mkdir /certs

WORKDIR /certs

RUN openssl req -new -x509 -nodes -out nginx.crt \
   -keyout nginx.key -subj '/CN=192.168.56.11.xip.io' -days 3650

VOLUME /certs
