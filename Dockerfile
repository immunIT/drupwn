# Dockerfile for https://github.com/immunIT/drupwn
# License GPLv3
FROM python:3.7-alpine3.9

COPY . /opt/drupwn

WORKDIR /opt/drupwn

RUN python setup.py install

ENTRYPOINT ["drupwn"]
CMD ["--help"]
