FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y byobu curl dnsutils groff iputils-ping net-tools telnet tree unzip vim wget \
    && cd /tmp \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && echo "AWS-CLI Version --> $(aws --version)"

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]