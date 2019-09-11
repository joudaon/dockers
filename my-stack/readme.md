# my-stack

This docker-compose file contains useful services that might be required by developers. 

Stored data will be placed in current directory under "./storeddata" folder.

## TOC

- [my-stack](#my-stack)
  - [TOC](#toc)
  - [Available services](#available-services)
  - [Services' versions](#services-versions)
  - [Ports](#ports)
  - [Elasticsearch](#elasticsearch)
  - [Commands](#commands)

## Available services

- cassandra (2 nodes)
- clickhouse (1 node)
- elasticsearch (1 node)
- kibana (1 node)
- hbase (1 node)
- hdfs (1 node)
- kafka (1 node)
- mongodb (1 node)
- redis (1 node)
- sqlserver (1 node)

## Services' versions

To change the version of a service, update the ".env" file.

## Ports

List of the services' ports.

| Service           | Port  |
| ----------------- |:-----:|
| cassandra         | 9042  |
| clickhouse-server | 9000  |
| elasticsearch     | 9200  |
| kibana            | 5601  |
| hbase (ui)        | 16010 |
| hadoop (ui)       | 50070 |
| zookeeper         | 2181  |
| kafka             | 9092  |
| mongodb           | 27017 |
| redis             | 6379  |
| sqlserver         | 1433  |


## Elasticsearch

Kibana username and password:
- user: elastic
- password: changeme

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
