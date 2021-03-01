# 03 MongoDB Create Collection
# 0303_check_if_collection_exists_specific_by_name.py

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")


