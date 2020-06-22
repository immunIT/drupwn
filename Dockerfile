FROM alpine:latest

RUN apk add --no-cache python3

ADD . /opt/drupwn

WORKDIR /opt/drupwn

RUN python3 setup.py install

ENTRYPOINT ["drupwn"]
CMD ["--help"]
