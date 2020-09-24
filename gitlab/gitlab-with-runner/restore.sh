#!/bin/bash

# Restores actual gitlab dir recursively. 
# Must be runned as root once docker is stopped.

sudo tar --same-owner -xf gitlab-backup-$(date +%F)