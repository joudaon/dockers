#!/bin/bash

# Backups actual gitlab dir recursively. 
# Must be runned as root once docker is stopped.

sudo tar -cpzf gitlab-backup-$(date +%F).tar .
