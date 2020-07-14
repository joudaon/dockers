#!/bin/bash

# Add the following at the start of your script. It will make the script exit when a command fails.
set -e
# Add the following to print out each commans befoee it’s executed (Debug).
set -x
# Add the following to return the exit code of the last command to exit with a non-zero status code (ie. error).
set -o pipefail

echo "[Entrypoint] AWS"

mkdir -p /root/.aws

echo "[default]" >> /root/.aws/credentials
echo "aws_access_key_id = $AWS_ACCESS_KEY_ID" >> /root/.aws/credentials
echo "aws_secret_access_key = $AWS_SECRET_ACCESS_KEY" >> /root/.aws/credentials
echo "region = $AWS_DEFAULT_REGION" >> /root/.aws/credentials
tail -f /dev/null

exec "$@"