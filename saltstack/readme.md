# saltstack

## TOC

- [saltstack](#saltstack)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker Salt-Master](https://github.com/thisissoon/Docker-Salt-Master)

## Information

This projects enables the generation of a Docker container with the desired saltstack version and run saltstack commands. We can mount a volume to run our own saltstack code files.

To make this work we run the following

```sh
# Start container
$> docker-compose up -d
# Getting salt installed components
$> salt-call --versions-report
```
