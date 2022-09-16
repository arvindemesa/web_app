#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

# Tell apt-get we're never going to be able to give manual
# feedback:
export DEBIAN_FRONTEND=noninteractive

# Update the package listing, so we know what package exist:
sudo apt-get update

# Install security updates:
sudo apt-get -y upgrade

# Install a new package, without unnecessary recommended packages:
sudo apt-get update \
 && sudo apt-get install unixodbc -y \
 && sudo apt-get install unixodbc-dev -y \
 && sudo apt-get install freetds-dev -y \
 && sudo apt-get install freetds-bin -y \
 && sudo apt-get install tdsodbc -y \
 && sudo apt-get install --reinstall build-essential -y \
 && sudo apt-get install libxml2-dev libxmlsec1-dev xmlsec1 -y

# Delete cached files we don't need anymore:
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*
