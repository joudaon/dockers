# terraform

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire datacenter. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

## TOC

- [terraform](#terraform)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [terraform official site](https://www.terraform.io/)

## Information

This projects enables the generation of a Docker container with the desired Terraform version and run Terraform commands. We can mount a volume to run our own terraform code files.

To make this work we run the following

```sh
# Start container
$> docker-compose up -d
# Get into the container
$> docker-compose exec terrafom /bin/bash
# Go to the mapped volumn directory and run terraform commands
$> cd /terraform
$> terraform init
```