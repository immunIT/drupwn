FROM alpine:latest

RUN apk update
RUN apk add --no-cache python3 \ 
	&& apk add --no-cache py3-setuptools

ADD . /opt/drupwn

WORKDIR /opt/drupwn

RUN python3 setup.py install

ENTRYPOINT ["drupwn"]
CMD ["--help"]
