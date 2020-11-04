# sqlserver

## TOC

- [sqlserver](#sqlserver)
  - [TOC](#toc)
  - [Definition](#definition)
  - [How to deploy](#how-to-deploy)
  - [Useful links](#useful-links)

## Definition

This examples uses python library to load data into sqlserver db.

## How to deploy

- Create the folder this way if you don't want to receive an error message:

    ```sh
    $> mkdir -p mssql; sudo chown 10001 mssql
    ```

- Deploy `docker-compose.yml` file.

- `sa` is the default username.

## Useful links

- [Docker hub: sqlserver (Official Image)](https://hub.docker.com/_/microsoft-mssql-server)
- [pymssql - DB-API interface to Microsoft SQL Serve](https://pypi.org/project/pymssql/)
- [SQL-Server 2019 docker container fails to start with -v option](https://github.com/microsoft/mssql-docker/issues/615)