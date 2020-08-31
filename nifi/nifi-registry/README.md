# nifi-registry

Registry—a subproject of Apache NiFi—is a complementary application that provides a central location for storage and management of shared resources across one or more instances of NiFi and/or MiNiFi.

Specific goals for the initial thrust of the Registry effort include:

- Implementation of a Flow Registry for storing and managing versioned flows
- Integration with NiFi to allow storing, retrieving, and upgrading versioned flows from a Flow Registry
- Administration of the Registry for defining users, groups, and policies

Future efforts may include capabilities to support additional registry concepts as they are identified by the community.

## TOC

- [nifi-registry](#nifi-registry)
  - [TOC](#toc)
  - [How to deploy](#how-to-deploy)
  - [Useful links](#useful-links)

## How to deploy

Deploy `docker-compose.yml` file and then access the web UI on: `http://localhost:18080/nifi-registry`. Maybe you have to wait for a while.

## Useful links

- [Official Site](https://nifi.apache.org/registry)
- [Docker hub](https://hub.docker.com/r/apache/nifi-registry)
