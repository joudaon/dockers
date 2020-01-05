#!/bin/bash

#
# Salt-Master Run Script
#

set -e

echo "--> [Entrypoint] Salt"

saltpath="/etc/salt"

if [[ "$SALT_INSTALL" ]]; then
    # Check if /etc/salt directory exist to check if salt is installed
    if [ -d "$saltpath" ]; then
        # Service already installed
        echo "<< Service $SALT_INSTALL already installed >>"
        echo "<< ------------------------------------- >>"
    else
        # Service not installed
        echo "<< Installing salt >>"
        apt-get -y install $SALT_INSTALL
        echo "<< Installing salt successful >>"
        echo "<< Starting service >>"
        service $SALT_INSTALL start
        echo "<< Displaying $saltpath folder >>"
        ls -alh $saltpath
        echo "<< Installation finished >>"
        echo "<< --------------------- >>"
    fi
fi

# if [[ "$SALT_INSTALL" == salt-minion ]]; then
#     echo "<< Updating minion configuration >>"
#     sed -i 's/#master: salt/master: saltmaster/g' /etc/salt/minion
#     service $SALT_INSTALL restart
# fi

tail -f /dev/null