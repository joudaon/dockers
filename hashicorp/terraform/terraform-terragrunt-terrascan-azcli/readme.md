# terraform docker image

Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions.

Configuration files describe to Terraform the components needed to run a single application or your entire datacenter. Terraform generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure. As the configuration changes, Terraform is able to determine what changed and create incremental execution plans which can be applied.

The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

This container contains the following tools:

- [Terraform](https://www.terraform.io/)  
  Use Infrastructure as Code to provision and manage any cloud, infrastructure, or service
- [Terragrunt](https://terragrunt.gruntwork.io/)  
  Terragrunt is a thin wrapper that provides extra tools for keeping your configurations DRY, working with multiple Terraform modules, and managing remote state.
- [Terrascan](https://github.com/accurics/terrascan)  
  Detect compliance and security violations across Infrastructure as Code to mitigate risk before provisioning cloud native infrastructure.
- [AZ-Cli](https://docs.microsoft.com/en-us/cli/azure/)  
  The Azure command-line interface (Azure CLI) is a set of commands used to create and manage Azure resources. The Azure CLI is available across Azure services and is designed to get you working quickly with Azure, with an emphasis on automation.

## TOC

- [terraform docker image](#terraform-docker-image)
  - [TOC](#toc)
  - [Information](#information)
  - [How to deploy](#how-to-deploy)
  - [Compatibility](#compatibility)
  - [Terraform](#terraform)
    - [Terraform variables](#terraform-variables)
    - [Using workspaces](#using-workspaces)

## Information

This projects enables the generation of a Docker container with the desired Terraform version and run Terraform commands. We can mount a volume to run our own terraform code files.

## How to deploy

1. Create a folder called `terraform` and place here all your files or update `docker-compose.yml` file `volume` tag to target a host folder with `terraform` and `terragrunt` files on your host.
2. Update values on `.env` file. 
   1. Enter `terraform`, `terragrunt` and `terrascan` versions you want to use.
   2. Enter Azure credentials which will enable `terraform` working with Azure after running `az login`.

3. Run the following commands:

    ```sh
    # Start container
    $> docker-compose up -d --build
    # Get into the container
    $> docker-compose exec terraform /bin/bash
    # Go to the mapped volume directory and run terraform commands
    $> cd /terraform
    $> terraform init
    ```

## Compatibility

This docker-compose file has been tested on:

- Ubuntu 18.04.5 LTS
- Docker 19.03.13 Community version
- docker-compose version 1.26.0

## Terraform

### Terraform variables

```json
variable "server_name" {
  type    = string
  default = "web-server"
}

variable "server_number" {
  type    = number
  default = 1
}

variable "provision_vm_agent" {
  type    = bool
  default = true
}

variable "servers" {
  type    = list(string)
  default = ["webserver1", "webserver2"]
}

variable "subnets" {
  type = map
  default = {
    web-server         = "1.0.1.0/24"
    AzureBastionSubnet = "1.0.2.0/24"
  }
}
```

### Using workspaces 

Add this on `main.tf` file:

```json
locals {
  environment = terraform.workspace
}
```

Then use the variable in the selected resources like this:

```json
resource "azurerm_resource_group" "web_server_rg" {
  name     = "${local.environment}-${var.web_server_rg}"
  location = var.web_server_location

  tags = {
    Environment = local.environment
    Team        = "DevOps"
  }
}
```

On the console change workspace:

```sh
$> terraform workspace new dev
$> terraform workspace list
$> terraform workspace select dev
```

Our `local.environment` value should be `dev`.
