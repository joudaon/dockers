FROM maven:3.6.0-jdk-11-slim AS build
COPY src /opt/app/src
COPY pom.xml /opt/app
RUN mvn -f /opt/app/pom.xml clean package

FROM tomcat:8.5-alpine
COPY --from=build /opt/app/target/demo.war /usr/local/tomcat/webapps/demo.war
EXPOSE 8080
