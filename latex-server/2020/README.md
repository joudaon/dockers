# 2020

This is the latest Sharelatex version.

It contains a Dockerfile which installs all Latex dependencies inside docker container.

## How to deploy 

```sh
# If we just want to build the image
$> docker build -t sharelatex-full:2.4.2 .
# Deploy everything
$> docker-compose up -d
```

## Username and password

When everything is up go to: `http://localhost/launchpad` to set up admin user.

## More information

- [Docker Sharelatex-full](https://hub.docker.com/r/t4skforce/sharelatex-full)
- [github overleaf](https://github.com/overleaf/overleaf/blob/master/docker-compose.yml)