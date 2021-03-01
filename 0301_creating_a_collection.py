# 03 MongoDB Create Collection
# 0301_creating_a_collection.py
# 
# Create a collection called "customers":

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
