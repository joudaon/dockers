# gitlab

## TOC

- [gitlab](#gitlab)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)
  - [Example .gitlab-ci.yml](#example-gitlab-ciyml)

## Useful links

- [GitLab Docker images](https://docs.gitlab.com/omnibus/docker/README.html)
- [Dockerhub](https://hub.docker.com/r/gitlab/gitlab-ce/)
- [Dockerfile gitlab](https://gitlab.com/gitlab-org/omnibus-gitlab/tree/master/docker)
- [Run GitLab Runner in a container](https://docs.gitlab.com/runner/install/docker.html)
- [Create a docker-compose file for fully running gitlab](https://gitlab.com/gitlab-org/gitlab-foss/issues/50851)
- [Create a docker-compose file for fully running gitlab](https://gitlab.com/gitlab-org/gitlab/issues/23911)
- [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/README.html)

## Information

Default gitlab username: root

## Example .gitlab-ci.yml

```yaml
image: docker:latest

services:
  - docker:dind

before_script:
  - docker info

build:
  stage: build
  script:
    - docker ps -a
```