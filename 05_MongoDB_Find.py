# 05_MongoDB_Find.py
# 
# Python MongoDB Find
# ===================
# In MongoDB we use the find() and findOne() methods to find data in a collection.
# 
# Just like the SELECT statement is used to find data in a table in a MySQL database.
# 
# Find One
# --------
# To select data from a collection in MongoDB, we can use the find_one() method.
# 
# The find_one() method returns the first occurrence in the selection.
# 
# Example: Find the first document in the customers collection:
# 
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# x = mycoll.find_one()
# 
# print(x)
# #### end ####
# 
# Find All
# --------
# To select data from a table in MongoDB, we can also use the find() method.
# 
# The find() method returns all occurrences in the selection.
# 
# The first parameter of the find() method is a query object.
# In this example we use an empty query object, which selects all documents in the collection.
# No parameters in the find() method gives you the same result as SELECT * in MySQL.
# 
# Example: Return all documents in the "customers" collection, and print each document:
# 
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# for x in mycoll.find():
#   print(x)
# #### end ####
# 
# Return Only Some Fields
# -----------------------
# The second parameter of the find() method is an object describing which fields to include in the result.
# 
# This parameter is optional, and if omitted, all fields will be included in the result.
# 
# Example: Return only the names and addresses, not the _ids:
# 
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# for x in mycoll.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)
# #### end ####
# 
# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field).
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:
# 
# Example: This example will exclude "address" from the result:
# 
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# for x in mycoll.find({},{ "address": 0 }):
#   print(x)
# #### end ####
# 
# Example: You get an error if you specify both 0 and 1 values in the same object
# (except if one of the fields is the _id field):
# 
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# 
# for x in mycol.find({},{ "name": 1, "address": 0 }):
#   print(x)
# #### end ####