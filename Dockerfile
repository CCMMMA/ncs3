FROM python:3.9-slim-buster

WORKDIR /ncs3

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app
COPY config.py config.py
COPY ncs3.py ncs3.py
COPY ncs3.sh ncs3.sh

ENTRYPOINT ["./ncs3.sh"]