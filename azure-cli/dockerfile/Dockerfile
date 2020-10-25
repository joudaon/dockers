FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y byobu curl dnsutils less groff iputils-ping net-tools telnet tree unzip vim wget \
    && echo "--> Installing Azure Cli..." \
    && apt-get -y install ca-certificates curl apt-transport-https lsb-release gnupg \
    && curl -sL https://packages.microsoft.com/keys/microsoft.asc | \
      gpg --dearmor | \
      tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null \
    && AZ_REPO=$(lsb_release -cs) \
      echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | \
      tee /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update \
    && apt-get install azure-cli \
    && echo "AZURE-CLI Version --> $(az version)"

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]