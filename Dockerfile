#
#Flask App Dockerfile

# Pull base image.
FROM centos:7.0.1406

# Build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel git
RUN easy_install pip
RUN mkdir /opt/learn
WORKDIR /opt/learn
ADD requirements.txt /opt/learn
MAINTAINER Aaron Michelson "michnoam@gmail.com"
RUN pip install -r requirements.txt
ADD . /opt/learn

# Define default command.
CMD ["python", "manage.py", "runserver"]

# to build: $ docker build -t lassee/learn:latest .
#$ docker run -d -p 5000:5000 flask-sample-one
#dockerdocker run -t -d -p 5000:5000 --name learn lassee/learn bash

# the -t is HUUUGE!
