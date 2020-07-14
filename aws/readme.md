# aws-cli

## TOC

- [aws-cli](#aws-cli)
  - [TOC](#toc)
  - [How it works](#how-it-works)
  - [Useful links](#useful-links)

## How it works

Get your AWS credentials and update `environment` values on `docker-compose.yml` file with your credentials.

Then,

```sh
# Start container
$> docker-compose up -d
# Go inside container
$> docker-compose exec aws-cli /bin/bash
# Inside container
$> aws help
$> aws iam create-user --user-name testuser
```

## Useful links

- [Docker hub: amazon/aws-cli (Official Image)](https://hub.docker.com/r/amazon/aws-cli)
- [Set up AWS Credentials and Region for Development](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html)
- [ckulka/awscli](https://github.com/ckulka/awscli/blob/master/docker-compose.example.yml)
