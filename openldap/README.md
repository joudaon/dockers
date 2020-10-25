# ldap-phpldapadmin

- [ldap-phpldapadmin](#ldap-phpldapadmin)
  - [Information](#information)
  - [Login information](#login-information)
  - [How to deploy](#how-to-deploy)
  - [Useful links](#useful-links)

## Information

OpenLDAP Software is an open source implementation of the Lightweight Directory Access Protocol.

## Login information 

Login:cn=admin,dc=example,dc=org

Password:"admin"

## How to deploy 

Deploy the `docker-compose` file

```sh
$> docker-compose up -d
```

Go to `http://localhost:8080` and login with above mentioned credentials.

There is a `sample.ldif` file which can be imported on the UI, under `import` option.

## Useful links

- [Docker hub: openldap (Official Image)](https://hub.docker.com/r/osixia/openldap/)
- [Github openldap](https://github.com/osixia/docker-openldap)
- [Official website](https://www.openldap.org/)
- [Docker OpenLDAP + phpldapadmin example](https://gist.github.com/thomasdarimont/d22a616a74b45964106461efb948df9c)
- [Tutorial: Setup OpenLDAP and configure clients](https://www.youtube.com/watch?v=p857CNi60LM&ab_channel=DrevonGaming)

