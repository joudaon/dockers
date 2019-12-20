FROM ubuntu:18.04

ARG PACKER_VERSION

RUN apt-get update \
    && apt-get install -y unzip vim wget byobu tree \
    && cd /tmp \
    && wget https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
    && unzip packer_${PACKER_VERSION}_linux_amd64.zip \
    && rm -rf packer_${PACKER_VERSION}_linux_amd64.zip \
    && mv packer /usr/local/bin/ \
    && echo "--> Packer version:" \
    && packer version

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
