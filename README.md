# DOCKERS

The aim of this repository is to collect useful docker-compose files with different services so that they can help other developers to ease their work.

Feel free to add your own or someone else's profile README if you find it super awesome! 

Don't forget to leave a ⭐ if you found this useful.

## TOC

- [DOCKERS](#dockers)
  - [TOC](#toc)
  - [Commands](#commands)
  - [Working with Dockerfiles](#working-with-dockerfiles)
  - [Useful links:](#useful-links)

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

Deleting all docker data

```sh
$> docker system prune -a
```

Copy file from container to host

```sh
$> docker cp <containerId>:/file/path/within/container /host/path/target
```

## Working with Dockerfiles

Building an image

```sh
$> docker build -t <imagename:tag> .
```

## Useful links:

- [Install Docker Engine on Ubuntu | Docker Documentation](https://docs.docker.com/engine/install/ubuntu/)
- [Install Docker Compose | Docker Documentation](https://docs.docker.com/compose/install/)
- [Compose file version 3 reference | Docker Documentation](https://docs.docker.com/compose/compose-file/)
- [Compose file version 2 reference | Docker Documentation](https://docs.docker.com/compose/compose-file/compose-file-v2/)
- [Installing the Docker client on Windows Subsystem for Linux (Ubuntu)](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4)
- [How To Change Docker Data Folder Configuration - Developer Space - Medium](https://medium.com/developer-space/how-to-change-docker-data-folder-configuration-33d372669056)
- [HOW TO KEEP DOCKER CONTAINERS RUNNING](http://bigdatums.net/2017/11/07/how-to-keep-docker-containers-running/)
- [What security concerns should I have with Docker? How should I go about locking it down? · Issue #17 · BretFisher/ama](https://github.com/BretFisher/ama/issues/17)
