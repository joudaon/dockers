# azure-cli

## TOC

- [azure-cli](#azure-cli)
  - [TOC](#toc)
  - [How it works](#how-it-works)
  - [Useful links](#useful-links)

## How it works

Get your AZURE credentials and update `environment` values on `docker-compose.yml` file with your credentials.

Then,

```sh
# Start container
$> docker-compose up -d
# Go inside container
$> docker-compose exec azure-cli /bin/bash
# Inside container
$> azure help
```

## Useful links
Install Azure CLI with apt](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt)
