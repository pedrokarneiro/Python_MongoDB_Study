# 02 MongoDB Create Database
# 0202_check_if_database_exists.py

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_databse_names())

