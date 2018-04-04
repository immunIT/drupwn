FROM debian:latest

RUN apt update
RUN apt -y install python3 python3-pip python-pkg-resources

ADD . /opt/drupwn
RUN pip3 install -r /opt/drupwn/requirements.txt

WORKDIR /opt/drupwn

ENTRYPOINT ["python3", "drupwn.py"]
CMD ["--help"]
