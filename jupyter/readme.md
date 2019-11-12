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

```sh
$> sudo chmod 666 /var/run/docker.sock
```

More information [here](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue).

## Docker useful links

- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
- [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)
- [mikebirdgeneau/jupyterlab](https://hub.docker.com/r/mikebirdgeneau/jupyterlab)
- [The Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/index.html)
