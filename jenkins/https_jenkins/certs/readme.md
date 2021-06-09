Create an ssl certificate to work with https:
```sh
$> openssl req -days 365 -nodes -new -x509 -keyout jenkins.key -out jenkins.crt -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department CN=example.com"
```