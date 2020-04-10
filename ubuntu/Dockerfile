ARG UBUNTU_VERSION

FROM ubuntu:$UBUNTU_VERSION

RUN apt-get update \
    && apt-get install -y byobu curl iputils-ping net-tools telnet tree unzip vim wget

CMD tail -f /dev/null