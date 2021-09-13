import sys
import argparse
import mysql.connector
import json
import os
import pdb

parser = argparse.ArgumentParser()
parser.add_argument('mysql_host', type=str, help='mysql host', default="mysqldb")
parser.add_argument('mysql_user', type=str, help='mysql user', default="root")
parser.add_argument('mysql_password', type=str, help='mysql password', default="p@ssw0rd1")
parser.add_argument('--database', type=str, default='partnet_anno_system', help='mysql database name [Default: partnet_anno_system]')
args = parser.parse_args()
# python mysql/import_into_mysql.py localhost root ******
in_dir = '/usr/src/app/storage/data/'

print(args)

mydb = mysql.connector.connect(
    host=args.mysql_host,
    user=args.mysql_user,
    passwd=args.mysql_password
)

assert mydb.is_connected()
# pdb.set_trace()
# read the db to get the existing records
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
dblist = [db[0] for db in mycursor]
# pdb.set_trace()
if 'partnet_anno_system' not in dblist:
    with open('/usr/src/app/server/mysql/create_table.sql', 'r') as f:
        query = f.read()
    mycursor.execute(query)
mycursor.execute("USE partnet_anno_system;")
mycursor.execute("SELECT modelID, categoryID FROM Model")
existing_records_in_db = [str(item[0])+'-'+str(item[1]) for item in mycursor.fetchall()]

# then, we import the non-existing records into the db
sql = "INSERT INTO Model (modelID, categoryID) VALUES (%s, %s)"

for catname in os.listdir(in_dir):
    if '.' not in catname:
        for modelid in os.listdir(os.path.join(in_dir, catname)):
            if '.' not in modelid:
                if modelid+'-'+catname in existing_records_in_db:
                    print('SKIP: inserting ', modelid+'-'+catname)
                    continue
        
            try:
                val = (modelid, catname)
                mycursor.execute(sql, val)
                mydb.commit()
                print('SUCCESS: inserting ', modelid+'-'+catname)
            except:
                print('ERROR: inserting ', modelid+'-'+catname)


