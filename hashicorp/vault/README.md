# vault

Secure, store and tightly control access to tokens, passwords, certificates, encryption keys for protecting secrets and other sensitive data using a UI, CLI, or HTTP API.

## TOC

- [vault](#vault)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [Docker Hub - Vault](https://hub.docker.com/_/vault)
- [Vault official site](https://www.vaultproject.io/)
- [Using Vault with docker-compose.yml](https://stackoverflow.com/questions/45171564/using-vault-with-docker-compose-file)
- [Docker Compose - Hashicorp's Vault and Consul](https://www.bogotobogo.com/DevOps/Docker/Docker-Vault-Consul.php)

## Information

```sh
# Start container
$> docker-compose up -d
# Get into the container
$> docker-compose exec vault sh
# Login
$> vault login ${roottoken}
# Vault status
$> vault status
```

```sh
$> mkdir -p volumes/{config,data,logs,policies}
$> sudo rm -rf volumes/{data,logs,policies}
```

root token: s.nqDhiPajzDFiqmmazGk7Az2L
key 1: Oj+tZLNuJcXWLxOPaI2sFtsvm3drVR0YW0rQ/kpYwI0=