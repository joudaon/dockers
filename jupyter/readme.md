# Jupyter

## TOC

- [Jupyter](#jupyter)
  - [TOC](#toc)
  - [What is Jupyter?](#what-is-jupyter)
  - [Preparing storeddata folder](#preparing-storeddata-folder)
  - [Creating a token with a password](#creating-a-token-with-a-password)
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

## Docker useful links

- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
- [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)
- [mikebirdgeneau/jupyterlab](https://hub.docker.com/r/mikebirdgeneau/jupyterlab)
- [The Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/index.html)
