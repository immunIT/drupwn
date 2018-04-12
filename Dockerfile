FROM alpine:latest

RUN apk update
RUN apk add python3

ADD . /opt/drupwn
RUN pip3 install -r /opt/drupwn/requirements.txt

WORKDIR /opt/drupwn

ENTRYPOINT ["python3", "drupwn.py"]
CMD ["--help"]
