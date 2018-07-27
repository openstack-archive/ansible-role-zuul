#!/bin/bash -xe

# This script will be run by OpenStack CI before unit tests are run,
# it sets up the test system as needed.
# Developers should setup their test systems in a similar way.
LSBDISTCODENAME=$(lsb_release -cs)

if type apt-get; then
    # Install https transport - otherwise apt-get HANGS on https urls
    sudo apt-get update
    sudo apt-get install -y apt-transport-https
    # Install recent NodeJS repo
    curl -sS https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add -
    echo "deb https://deb.nodesource.com/node_8.x $LSBDISTCODENAME main" | sudo tee /etc/apt/sources.list.d/nodesource.list
    # Install yarn repo
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
    sudo apt-get update
    sudo DEBIAN_FRONTEND=noninteractive \
        apt-get -q --option "Dpkg::Options::=--force-confold" --assume-yes \
        install nodejs yarn
fi
