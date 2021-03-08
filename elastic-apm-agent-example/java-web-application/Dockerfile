FROM maven:3.6.0-jdk-11-slim AS build
COPY src /opt/app/src
COPY pom.xml /opt/app
RUN mvn -f /opt/app/pom.xml clean package

FROM tomcat:8.5-alpine
COPY --from=build /opt/app/target/demo.war /usr/local/tomcat/webapps/demo.war
RUN wget -O /opt/elastic-apm-agent-1.21.0.jar https://search.maven.org/remotecontent?filepath=co/elastic/apm/elastic-apm-agent/1.21.0/elastic-apm-agent-1.21.0.jar
EXPOSE 8080

CMD ["catalina.sh", "run"]