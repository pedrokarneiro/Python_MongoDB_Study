# 0504_MongoDB_Find_find_wo_ids.py
# 
# Python MongoDB Find - find() method example 3 - Excluding fields from selection
# -------------------------------------------------------------------------------
# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field).
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:
# 
# Example: This example will exclude (only) "address" from the result:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

for record in mycoll.find({},{ "address": 0 }):
  print(record)
