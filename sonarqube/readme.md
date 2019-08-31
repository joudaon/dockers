# sonarqube

## TOC

- [sonarqube](#sonarqube)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker hub: sonarqube (Official Image)](https://hub.docker.com/_/sonarqube/)
- [Docker hub: postgres (Official Image)](https://hub.docker.com/_/postgres)

## Information

All created folders need sudo chown 777 privileges before creating containers.

```sh
$> sudo mkdir sonarqube_conf sonarqube_data sonarqube_extensions sonarqube_bundled-plugins postgresql postgresql_data
$> sudo chmod 777 sonarqube_conf sonarqube_data sonarqube_extensions sonarqube_bundled-plugins postgresql postgresql_data
$> sudo rm -rf sonarqube_conf sonarqube_data sonarqube_extensions sonarqube_bundled-plugins postgresql postgresql_data
```

Default login credentials ([More information](https://docs.sonarqube.org/latest/instance-administration/security/)):

user: admin

password: admin

Once dockers are deployed, please go to: http://localhost/9000
