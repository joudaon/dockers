FROM docker.elastic.co/apm/apm-server:7.11.1
COPY apm-server.yml /usr/share/apm-server/apm-server.yml
USER root
RUN chown root:apm-server /usr/share/apm-server/apm-server.yml && \
    chmod go-w /usr/share/apm-server/apm-server.yml && \
    ls -alh /usr/share/apm-server/
USER apm-server