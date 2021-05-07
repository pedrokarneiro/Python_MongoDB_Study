# 0501_MongoDB_Find_find_one.py
# 
# Python MongoDB Find - find_one() method example
# -----------------------------------------------
# Example: Find the first document in the customers collection:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

x = mycoll.find_one()

print(x)
