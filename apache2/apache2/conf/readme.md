Create an ssl certificate to work with https:
```sh
$> openssl req  -nodes -new -x509  -keyout server.key -out server.cert -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department CN=example.com"
```