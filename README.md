# DOCKERS

Useful docker-compose files with different services.

## TOC

- [DOCKERS](#dockers)
  - [TOC](#toc)
  - [Commands](#commands)

## Commands

Create and start containers
```sh
$> docker-compose up
$> docker-compose up -d #Detached mode: Run containers in the background, print new container names.
```

Stop and remove containers, networks, images, and volumes
```sh
$> docker-compose down
```

Execute a command in a running container
```sh
$> docker-compose exec <servicename> sh #Get into container
$> docker-compose exec <servicename> /bin/bash #Get into container
$> docker-compose exec <servicename> pwd #Run command and exit
```

View output from containers.
```sh
$> docker-compose logs
$> docker-compose logs -f #View output from containers.
```

Stop and remove all docker containers
```sh
$> docker stop $(docker ps -a -q)
$> docker rm $(docker ps -a -q)
```

Remove all docker images
```sh
$> docker rmi $(docker images -q)
```

Deleting all the volumes

Once all the containers are deleted, you can delete all the Docker volumes on your computer using the following command

```sh
$> docker volume prune
```
