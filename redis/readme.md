# Redis

## TOC

- [Redis](#redis)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Useful commands](#useful-commands)

## Useful links

- [Setting up a Redis test environment using Docker Compose](https://cheesyprogrammer.com/2018/01/04/setting-up-a-redis-test-environment-using-docker-compose/)
- [redis 3.3.4](https://pypi.org/project/redis/)
- [redis official docker image](https://hub.docker.com/_/redis)

## Useful commands

```sh
# Get into redis container
$> docker exec -ti redis /bin/bash
# Go to binaries
$> cd /usr/local/bin
# Connect to redis
$> /usr/local/bin/redis-cli -h localhost -p 6379
# Insert key
$> set mykey "hello"
# Get key
$> get mykey
```