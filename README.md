# DOCKERS

Useful docker-compose files with different services.

## Commands

Create and start containers
```sh
$ docker-compose up
$ docker-compose up -d #Detached mode: Run containers in the background, print new container names.
```

Stop and remove containers, networks, images, and volumes
```sh
$ docker-compose down
```

Execute a command in a running container
```sh
$ docker-compose exec <servicename> sh #Get into container
$ docker-compose exec <servicename> pwd #Run command and exit
```

View output from containers.
```sh
$ docker-compose logs
$ docker-compose logs -f #View output from containers.
```

Stop and remove all docker containers
```sh
$ docker stop $(docker ps -a -q)
$ docker rm $(docker ps -a -q)
```

Remove all docker images
```sh
$ docker rmi $(docker images -q)
```
