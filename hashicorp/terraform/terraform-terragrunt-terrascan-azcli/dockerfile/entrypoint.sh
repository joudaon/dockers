#!/bin/bash

# Add the following at the start of your script. It will make the script exit when a command fails.
set -e
# Add the following to print out each commans befoee it’s executed (Debug).
set -x
# Add the following to return the exit code of the last command to exit with a non-zero status code (ie. error).
set -o pipefail

echo "[Entrypoint] Terraform"

az login -u $AZ_USERNAME -p $AZ_PASSWORD

tail -f /dev/null

exec "$@"
