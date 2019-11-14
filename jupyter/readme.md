# Jupyter

## TOC

- [Jupyter](#jupyter)
  - [TOC](#toc)
  - [What is Jupyter?](#what-is-jupyter)
  - [Preparing storeddata folder](#preparing-storeddata-folder)
  - [Creating a token with a password](#creating-a-token-with-a-password)
  - [Enabling docker inside the container](#enabling-docker-inside-the-container)
  - [Docker useful links](#docker-useful-links)

## What is Jupyter?

Project Jupyter exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.

## Preparing storeddata folder

```sh
$> mkdir -p storeddata/work/
```

## [Creating a token with a password](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)

```python
In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

## Enabling docker inside the container

Run on the host:

By default host values on /var/run/docker.sock are:

```sh
srw-rw----  1 root  docker    0 Nov 13 20:39 docker.sock=
```

We go inside the container and the default values are: 

```sh
srw-rw---- 1 root  999    0 Nov 13 19:39 docker.sock
```

Now we run the following inside the container:

```sh
$> sudo groupadd docker
$> sudo usermod -aG docker jovyan
$> sudo chown jovyan:docker docker.sock
```

The values change to:

```sh
# Inside the container
srw-rw---- 1 jovyan docker    0 Nov 13 19:39 docker.sock=
# On the host
srw-rw----  1 joudaon joudaon    0 Nov 13 20:39 docker.sock=
```

We can test that docker works inside the container by:

Install docker with pip:

```sh
$> pip install docker
```

Run the following lines in python:

```python
import docker
client = docker.from_env()
client.images.list()
```

More information [here](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue).

## Docker useful links

- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
- [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)
- [mikebirdgeneau/jupyterlab](https://hub.docker.com/r/mikebirdgeneau/jupyterlab)
- [The Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/index.html)
