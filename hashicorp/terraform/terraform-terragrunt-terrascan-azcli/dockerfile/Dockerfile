FROM ubuntu:18.04

ARG TERRAFORM_VERSION 
ARG TERRAGRUNT_VERSION
ARG TERRASCAN_VERSION

# Install Basic packages
RUN apt-get update \
    && apt-get install -y byobu curl dnsutils git iputils-ping less net-tools telnet tree unzip vim wget

# Install Terraform
RUN cd /tmp \
    && wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/ \
  && echo "Terraform Version --> $(terraform version)"

# Install Terragrunt
RUN cd /tmp \
    && wget https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 \
    && mv terragrunt_linux_amd64 terragrunt \
    && chmod u+x terragrunt \
    && mv terragrunt /usr/local/bin/terragrunt \
    && echo "Terragrunt Version --> $(terragrunt -v)"

# Install Terrascan - https://github.com/accurics/terrascan
RUN cd /tmp \
    && curl --location https://github.com/accurics/terrascan/releases/download/v${TERRASCAN_VERSION}/terrascan_${TERRASCAN_VERSION}_Linux_x86_64.tar.gz --output terrascan.tar.gz \
    && tar -xvf terrascan.tar.gz \
    && rm -rf terrascan.tar.gz \
    && install terrascan /usr/local/bin \
    && rm -rf * \
    && echo "Terrascan Version --> $(terrascan version)"

# Install azure-cli
RUN echo "--> Installing Azure Cli..." \
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
