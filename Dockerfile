FROM ubuntu:16.04

ENV LANG C.UTF-8
RUN apt-get update && apt-get install -y python python-dev python2.7 python-pip virtualenv libssl-dev libpq-dev git build-essential libfontconfig1 libfontconfig1-dev
RUN pip install setuptools pip --upgrade --force-reinstall requests

COPY * /

ENTRYPOINT ["python", "run.py"]

