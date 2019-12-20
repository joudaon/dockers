# packer

Packer is an open source tool for creating identical machine images for multiple platforms from a single source configuration. Packer is lightweight, runs on every major operating system, and is highly performant, creating machine images for multiple platforms in parallel. Packer does not replace configuration management like Chef or Puppet. In fact, when building images, Packer is able to use tools like Chef or Puppet to install software onto the image.

A machine image is a single static unit that contains a pre-configured operating system and installed software which is used to quickly create new running machines. Machine image formats change for each platform. Some examples include AMIs for EC2, VMDK/VMX files for VMware, OVF exports for VirtualBox, etc.

## TOC

- [packer](#packer)
  - [TOC](#toc)
  - [Useful links](#useful-links)
  - [Information](#information)

## Useful links

- [packer official site](https://www.packer.io/)

## Information

This projects enables the generation of a Docker container with the desired packer version and run packer commands. We can mount a volume to run our own packer code files.

To make this work we run the following

```sh
# Start container
$> docker-compose up -d
# Get into the container
$> docker-compose exec packer /bin/bash
# Go to the mapped volume directory and run packer commands
$> cd /packer
$> packer validate {file}.json
$> packer build {file}.json
```
