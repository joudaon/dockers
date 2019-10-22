# nginx

## TOC

- [nginx](#nginx)
  - [TOC](#toc)
  - [Useful links](#useful-links)

## Useful links

- [Docker hub: nginx (Official Image)](https://hub.docker.com/_/nginx)
- [Setting up a Reverse-Proxy with Nginx and docker-compose](https://dev.to/domysee/setting-up-a-reverse-proxy-with-nginx-and-docker-compose-29jg)
- [Official build of Nginx.](https://docs.docker.com/samples/library/nginx/)
- [Cómo crear un certificado SSL (activar https) en Nginx para Ubuntu 14.04 o Debian](http://alejovazquez.blogspot.com/2015/04/como-crear-un-certificado-ssl-activar.html)

Create an ssl certificate to work with https:
```sh
$> openssl req  -nodes -new -x509  -keyout server.key -out server.cert -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department CN=example.com"
```