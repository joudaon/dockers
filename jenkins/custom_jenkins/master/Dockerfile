ARG JENKINS_VERSION

FROM jenkins/jenkins:$JENKINS_VERSION

ARG JENKINS_USER 
ARG JENKINS_PASS

# if we want to install via apt
USER root
RUN apt-get update \
    && apt-get install -y byobu curl iputils-ping net-tools telnet tree unzip vim wget
# drop back to the regular jenkins user - good practice
USER jenkins

# Installing pluings
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

ENV JENKINS_USER $JENKINS_USER
ENV JENKINS_PASS $JENKINS_PASS

# '*.groovy' files placed at /usr/share/jenkins/ref/init.groovy.d/
# will execute custom configurations settings
COPY init.groovy.d /usr/share/jenkins/ref/init.groovy.d/

VOLUME /var/jenkins_home