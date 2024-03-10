#!/bin/bash
# install docker on centos

echo "start install docker"
# uninstall old versions
sudo yum remove docker \
docker-client \
docker-client-latest \
docker-common \
docker-latest \
docker-latest-logrotate \
docker-logrotate \
docker-engine
# setup repo
sudo yum install -y yum-utils
sudo yum-config-manager \
        --add-repo \
            https://download.docker.com/linux/centos/docker-ce.repo
# setup nightly repo
sudo yum-config-manager --enable docker-ce-nightly
# enable test channel
sudo yum-config-manager --enable docker-ce-test

# You can disable the nightly or test repository by running 
# the yum-config-manager command with the --disable flag. 
# To re-enable it, use the --enable flag. 
# The following command disables the nightly repository.

sudo yum-config-manager --disable docker-ce-nightly
# Install the latest version of Docker Engine and containerd, 
# or go to the next step to install a specific version:

sudo yum install docker-ce docker-ce-cli containerd.io

# start docker
sudo systemctl start docker
# verify docker engine is ok by run the docker-helloworld
sudo docker run hello-world
