FROM jenkins/jenkins:2.204.2

# if we want to install via apt
USER root
RUN apt-get update \
    && apt-get install -y byobu curl iputils-ping net-tools telnet tree unzip vim wget
# drop back to the regular jenkins user - good practice
USER jenkins

# Installing pluings
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Setting custom executor number
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy
