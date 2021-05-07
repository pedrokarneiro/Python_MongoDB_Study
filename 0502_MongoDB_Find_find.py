# 0502_MongoDB_Find_find.py
# 
# Python MongoDB Find - find() method example
# -------------------------------------------
# To select data from a table in MongoDB, we can also use the find() method.
# The find() method returns ALL occurrences in the selection.
# The first parameter of the find() method is a query object.
# In this example we use an empty query object, which selects all documents in the collection.
# No parameters in the find() method gives you the same result as SELECT * (with no WHERE clause) in regular SQL.
# 
# Example: Return all documents in the "customers" collection, and print each document:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

for doc in mycoll.find():
  print(doc)

