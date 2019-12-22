FROM ubuntu:16.04

ARG SALT_VERSION

RUN apt-get update \
    && apt-get install -y byobu curl iputils-ping net-tools telnet tree unzip vim wget \
    && wget -O - https://repo.saltstack.com/py3/ubuntu/16.04/amd64/archive/${SALT_VERSION}/SALTSTACK-GPG-KEY.pub | apt-key add - \
    && touch /etc/apt/sources.list.d/saltstack.list \
    && echo "deb http://repo.saltstack.com/py3/ubuntu/16.04/amd64/archive/${SALT_VERSION} xenial main" >> /etc/apt/sources.list.d/saltstack.list \
    && apt-get update

COPY entrypoint.sh /entrypoint.sh

EXPOSE 4505 4506

ENTRYPOINT ["/entrypoint.sh"]
