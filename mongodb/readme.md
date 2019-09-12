# mongodb

## TOC

- [mongodb](#mongodb)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker hub: mysql (Official Image)](https://hub.docker.com/_/mongo)
- [Docker docs](https://docs.docker.com/samples/library/mongo/)
- [Docker-Compose MongoDB](https://linuxhint.com/docker_compose_mongodb/)

## Information

Mongodb default installation dir is: /usr/bin

```sh
# Get into mongodb container
$> docker-compose exec mongodb /bin/bash
```

```sh
# Get into mongodb
$> /usr/bin/mongo
# Display databases
$(mongo)> db
```
