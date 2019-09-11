FROM docker:dind

RUN apk add --no-cache py-pip python-dev libffi-dev openssl-dev gcc libc-dev make && \
    pip install docker-compose && \
    mkdir -p /etc/docker/certs.d && \
    touch /etc/docker/daemon.json && \
    echo $'{ \n\ 
        "insecure-registries": [ \n\ 
        "harbor.ode.local" \n\ 
        ] \n\ 
        }' > /etc/docker/daemon.json && \
    touch /etc/docker/certs.d/ca.crt && \
    echo $'-----BEGIN CERTIFICATE----- \n\ 
        kñfdajfaoijñldlñmifdñjldja \n\
        -----END CERTIFICATE-----' > /etc/docker/certs.d/ca.crt
