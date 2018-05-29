FROM alpine:latest

RUN apk update
RUN apk add python3

ADD . /opt/drupwn

WORKDIR /opt/drupwn

RUN python3 setup.py install

ENTRYPOINT ["drupwn"]
CMD ["--help"]
