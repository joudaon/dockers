# docker

## TOC

- [docker](#docker)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker hub: docker - base-notebook (Official Image)](https://hub.docker.com/_/docker)
- [Docker hub: compose - base-notebook (Official Image)](https://hub.docker.com/r/docker/compose/)
- [Docker with Docker Compose image](https://github.com/tiangolo/docker-with-compose)
- [Using Docker-in-Docker for your CI or testing environment? Think twice.](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)
- [Docker-in-Docker](https://github.com/jpetazzo/dind)

## Information

There are 2 'docker-compose.yml" files. 
- docker-compose-with-just-docker.yml: builds a container with docker instaled inside it.
- docker-compose-with-docker-and-docker-compose.yml: uses 'Dockerfile' file to build a container with docker and docker-compose inside it.

To run docker inside container:

```sh
# Get into container
$> docker exec -ti docker /bin/sh
```
