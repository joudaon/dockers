# sonarqube

## TOC

- [sonarqube](#sonarqube)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker hub: sonarqube (Official Image)](https://hub.docker.com/_/sonarqube/)
- [Docker hub: postgres (Official Image)](https://hub.docker.com/_/postgres)
- [max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]](https://github.com/SonarSource/docker-sonarqube/issues/282)

## Information

All created folders need sudo chown 777 privileges before creating containers.

```sh
$> sudo mkdir sonarqube_conf sonarqube_data sonarqube_extensions sonarqube_bundled-plugins postgresql postgresql_data
$> sudo chmod 777 sonarqube_conf sonarqube_data sonarqube_extensions sonarqube_bundled-plugins postgresql postgresql_data
$> sudo rm -rf sonarqube_conf sonarqube_data sonarqube_extensions sonarqube_bundled-plugins postgresql postgresql_data
```

To fix "max virtual memory areas vm.max_map.count error, run the following as root user.

```sh
sysctl -w vm.max_map_count=262144
```

Default login credentials ([More information](https://docs.sonarqube.org/latest/instance-administration/security/)):

user: admin

password: admin

Once dockers are deployed, please go to: http://localhost/9000
