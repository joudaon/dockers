FROM jenkins/jenkins:2.204.4

# if we want to install via apt
USER root
RUN apt-get update \
    && apt-get install -y byobu curl iputils-ping net-tools telnet tree unzip vim wget
# drop back to the regular jenkins user - good practice
USER jenkins

# Installing pluings
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

ENV JENKINS_USER admin
ENV JENKINS_PASS admin

# Setting custom executor number
COPY init.groovy.d /usr/share/jenkins/ref/init.groovy.d/

VOLUME /var/jenkins_home