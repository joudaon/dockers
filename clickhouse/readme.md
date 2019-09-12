# clickhouse

## TOC

- [clickhouse](#clickhouse)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker hub: clickhouse (Official Image)](https://hub.docker.com/r/yandex/clickhouse-server/)
- [ClickHouse Server Docker Image](https://github.com/yandex/ClickHouse/tree/master/docker/server)
- [Clickouse Docker Compose](https://github.com/rongfengliang/clickhouse-docker-compose)
- [creating db and tables in a dockerized Clickhouse instance from docker-compose file
](https://stackoverflow.com/questions/52198099/creating-db-and-tables-in-a-dockerized-clickhouse-instance-from-docker-compose-f)

## Information

```sh
# Get into clickhouse-server container
$> docker-compose exec clickhouse-server /bin/bash
```

```sh
# Get into clickhouse-server
$> clickhouse-client
# Display databases
$(clickhouse_client)> show tables
```
