# 0503_MongoDB_Find_find_w_fields.py
# 
# Python MongoDB Find - find() method example 2 - Return only some fields (like not selecting *)
# ----------------------------------------------------------------------------------------------
# Return Only Some Fields
# -----------------------
# The second parameter of the find() method is an object describing which fields to include in the result.
# This parameter is optional, and if omitted, all fields will be included in the result (select *).
# 
# Example: Return only the names and addresses, not the _ids:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

for doc in mycoll.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(doc)

