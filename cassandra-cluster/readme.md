# cassandra-cluster

## TOC

- [cassandra-cluster](#cassandra-cluster)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker hub: cassandra (Official Image)](https://hub.docker.com/_/mongo)
- [Docker docs](http://abiasforaction.net/apache-cassandra-cluster-docker/)

## Information

```sh
# Get into mongodb container
$> docker exec -ti cassandra01 /bin/bash
```

```sh
# Display nodes in the cluster
$> nodetool status
# Display databases
$> cqlsh 127.0.0.1
```
