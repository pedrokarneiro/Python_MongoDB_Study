# 04 - MongoDB Insert
# 0401_insert_into_collection.py
# 
# Insert Into Collection
# ----------------------
# To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
# 
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field
# in the document you want to insert.
# 
# Example
# Insert a record in the "customers" collection:

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]
mydict = {"name": "John", "address": "Highway 37"}
result = mycoll.insert_one(mydict) # The insert_one() method returns a InsertOneResult object.
print(result) # Will print the object, something like "<pymongo.results.InsertOneResult object at 0x03D62918>"
