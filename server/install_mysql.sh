#!/usr/bin/bash

# Description: Script to install mysql server in docker
cd /tmp

curl -OL https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb
dpkg -i mysql-apt-config*
apt update
rm mysql-apt-config*
apt install mysql-server