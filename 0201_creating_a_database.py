# 02 MongoDB Create Database
# 0201_creating_a_database.py

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mtdatabase"]
