# 0505_MongoDB_Find_find_w_fields_error.py
# 
# Python MongoDB Find - find() method example 4 - Wrong fields exclusion from selection
# -------------------------------------------------------------------------------------
# You get an error if you specify both 0 and 1 values in the same object
# (except if one of the fields is the _id field):

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for line in mycol.find({},{ "name": 1, "address": 0 }):
  print(line)
