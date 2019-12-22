#!/bin/bash

#
# Salt-Master Run Script
#

set -e

echo "--> [Entrypoint] $SALT_INSTALL"

if [[ "$SALT_INSTALL" ]]; then
    echo "<< Installing salt >>"
    apt-get -y install $SALT_INSTALL
    echo "<< Installing salt successful >>"
    echo "<< Starting service >>"
    service $SALT_INSTALL start
    echo "<< Displaying /etc/salt folder >>"
    ls -alh /etc/salt
fi

# if [[ "$SALT_INSTALL" == salt-minion ]]; then
#     echo "<< Updating minion configuration >>"
#     sed -i 's/#master: salt/master: saltmaster/g' /etc/salt/minion
#     service $SALT_INSTALL restart
# fi

tail -f /dev/null