#!/usr/bin/bash
apt-get update && apt-get install build-essentials curl python3-dev python3-pip

# downloading nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
source ~/.bashrc
nvm install node

# using npm to install package
npm install

# installing mysql connector
pip install mysql-connector-python

# installing mysql server
# ./install_mysql.sh

# running mysql to create a database with the new table requirements
mysql -u root -p < mysql/create_table.sql

# importing using python to mysql
python mysql/import_into_mysql.py
