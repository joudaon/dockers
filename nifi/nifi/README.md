# nifi

NIFI, it is a software developed by Apache and available under open source license helps in data-flow, i.e. fetching data and sending data. It is like the processor of data, that takes input, process and give output, and vice versa.

The data processing be like getting data from some rest API, converting the fields to fields required, fetching specific fields or getting a single field. You can do this easily.

## TOC

- [nifi](#nifi)
  - [TOC](#toc)
  - [How to deploy](#how-to-deploy)
    - [Single node mode](#single-node-mode)
    - [Cluster mode](#cluster-mode)
      - [Version 1](#version-1)
      - [Version 2](#version-2)
  - [Templates](#templates)
  - [File transfer example](#file-transfer-example)
  - [Useful links](#useful-links)

## How to deploy

### Single node mode

Deploy `docker-compose.yml` file and then access the web UI on: `http://localhost:8080/nifi`. Maybe you have to wait for a while.

### Cluster mode

When deploying NiFi on `cluster mode` data on the UI should be replicated among all the replicas.

#### Version 1

Deploy cluster with the following command:

```sh
$> docker-compose up --scale nifi=3 -d
```

Then access web UI on: `http://localhost:32771/nifi/` after waiting for a while.

#### Version 2

Deploy `docker-compose.yml` file and then access the web UI on: `http://localhost:{8080:8081:8082}/nifi`. Maybe you have to wait for a while.

## Templates

There is a `templates` folder. These templates can be imported into Nifi. These templates can be donwload from [this](https://cwiki.apache.org/confluence/display/NIFI/Example+Dataflow+Templates) url. Also you can create your own ones and save them.

## File transfer example

This is a simple example that demonstrates how to transfer files inside a folder from source folder to a destination folder.

To do so, we have mounted `storeddata/input` and `storeddata/output` folders to docker. These folders need to be created before running `docker-compose` to get right permissions inside the container.

```sh
$> mkdir -p storeddata/input storeddata/output
```

Next, we deploy the container:

```sh
$> docker-compose up -d
```

On the NiFi UI we import `Get_and_Put_file.xml` and we start both `Processors` (`GetFile` and `PutFile`).

Now we have to place files into `storeddata/input` folder. We can do it with the following command:

```sh
$> for i in {1..5}; do echo "Hello world $i" > storeddata/input/test$i.txt; sleep 5 ; done
```

This will place 5 files inside `storeddata/input` and will be consumed and moved to `storeddata/output` folder.

## Useful links

- [Official Site](https://nifi.apache.org/)
- [Docker hub](https://hub.docker.com/r/apache/nifi)
- [Running NIFI in docker using docker-compose](https://medium.com/@erbalvindersingh/running-nifi-in-docker-using-docker-compose-34032de853d2)
- [Running a cluster with Apache Nifi and Docker](https://www.theninjacto.xyz/Running-cluster-Apache-Nifi-Docker/)
- [Running a cluster with Apache Nifi and Docker](https://www.nifi.rocks/apache-nifi-docker-compose-cluster/)
- [apache-nifi-templates](https://github.com/learnwithmanoj/apache-nifi-templates)