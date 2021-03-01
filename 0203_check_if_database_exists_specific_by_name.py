# 02 MongoDB Create Database
# 0203_check_if_database_exists_specific_by_name.py

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

