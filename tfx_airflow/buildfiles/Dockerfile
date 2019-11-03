FROM ubuntu:16.04
LABEL maintainer="tensorflow-extended-dev@googlegroups.com"

COPY init.sh /
COPY setup_demo.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils

RUN apt-get install -y --no-install-recommends \
        locales

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get install -y --no-install-recommends \
        python-pip \
        python3-pip \
        python3-dev \
        virtualenv \
        git \
        sudo \
        vim \
        wget \
        curl \
        build-essential \
        software-properties-common \
        default-jre \
        && apt-get autoclean \
        && apt-get autoremove --purge \
        && chmod +x /init.sh \
        && bash /init.sh

EXPOSE 4040 6006 8080 8081 8099 8888 
