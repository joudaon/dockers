# selenium grid

Deploy the environment:

```sh
$> docker-compose up -d
```

Go to: `http://localhost:4444/ui/index.html#/`

Go into python container:

```sh
$> docker-compose exec python3 /bin/bash
```

Run the script:

```sh
$> python3 test.py
```

## Useful links:

- [Selenium Grid With Docker](https://medium.com/@nitinbhardwaj6/selenium-grid-with-docker-c8ecb0d8404)
- [Getting Started with Docker Compose](https://github.com/SeleniumHQ/docker-selenium/wiki/Getting-Started-with-Docker-Compose)
- [Docker images for the Selenium Grid Server](https://github.com/SeleniumHQ/docker-selenium)
- [docker-selenium/docker-compose-v2.yml](https://github.com/SeleniumHQ/docker-selenium/blob/trunk/docker-compose-v2.yml)