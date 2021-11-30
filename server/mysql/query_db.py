# write random queries here!

import sys
import argparse
import mysql.connector
import json
import os
import pdb

# parser = argparse.ArgumentParser()
# parser.add_argument('mysql_host', type=str, help='mysql host', default="mysqldb")
# parser.add_argument('mysql_user', type=str, help='mysql user', default="root")
# parser.add_argument('mysql_password', type=str, help='mysql password', default="p@ssw0rd1")
# parser.add_argument('--database', type=str, default='partnet_anno_system', help='mysql database name [Default: partnet_anno_system]')
# args = parser.parse_args()
# python mysql/import_into_mysql.py localhost root ******
in_dir = '/usr/src/app/storage/data/'

# print(args)

mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    passwd="p@ssw0rd1"
)
assert mydb.is_connected()
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
pdb.set_trace()
mycursor.execute("USE partnet_anno_system;")

#mycursor.execute("DELETE FROM Annotation WHERE modelID='best_one'")
#mycursor.execute("DELETE FROM Model WHERE modelID='best_one'")
#mycursor.execute("DELETE FROM Annotation WHERE modelID = 'best_one' AND workerID = 'kanye'")