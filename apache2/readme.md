# tomcat

## TOC

- [tomcat](#tomcat)
  - [TOC](#toc)
  - [Useful links](#useful-links)

## Useful links

- [Docker hub: tomcat (Official Image)](https://hub.docker.com/_/tomcat)
- [Docker en proyectos Java (I). Cómo desplegar una aplicación Java en tomcat usando Docker](https://eckelon.net/desarrollo/2017/01/15/tomcat-y-docker.html)
- [Creating Self-Signed SSL Certificates For Apache On Linux](https://www.linux.com/tutorials/creating-self-signed-ssl-certificates-apache-linux/)
- [Is it possible to generate RSA key without pass phrase?](https://serverfault.com/questions/366372/is-it-possible-to-generate-rsa-key-without-pass-phrase/366373#366373)
- [HowTo: Create CSR using OpenSSL Without Prompt (Non-Interactive)](https://www.shellhacks.com/create-csr-openssl-without-prompt-non-interactive/)
- [WebSec Apache httpd Container](https://github.com/chrludwig/websec-apache-container)

Creating an ssl certificate:
```sh
$> openssl req  -nodes -new -x509  -keyout server.key -out server.cert -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department CN=example.com"
```