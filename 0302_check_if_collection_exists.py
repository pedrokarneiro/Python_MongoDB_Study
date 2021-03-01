# 03 MongoDB Create Collection
# 0302_check_if_collection_exists.py

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(mydb.list_collection_names())
