FROM teeratpitakrat/docker-locust
MAINTAINER Teerat Pitakrat

RUN sudo apt-get -y install python-pip
RUN sudo pip install influxdb

ADD ./test /test
ENV SCENARIO_FILE /test/locustfile.py
