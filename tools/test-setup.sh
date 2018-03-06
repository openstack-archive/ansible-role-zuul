#!/bin/bash -xe

# This script will be run by OpenStack CI before unit tests are run,
# it sets up the test system as needed.
# Developers should setup their test systems in a similar way.

# On fedora we need to copy sample config
if [ -f /etc/zookeeper/zoo_sample.cfg ]; then
    sudo cp /etc/zookeeper/zoo_sample.cfg /etc/zookeeper/zoo.cfg
fi

# Be sure zookeeper is started.
sudo service zookeeper start
