# 04 - MongoDB Insert
# 0402_insert_into_coll_return_id_field.py
# Return the _id Field
# --------------------
# The insert_one() method returns a InsertOneResult object, which has a property, inserted_id,
# that holds the id of the inserted document.
# 
# Example
# Insert another record in the "customers" collection, and return the value of the _id field:

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient("mydatabase")
mycoll = mydb["customers"]
mydict = {"name": "Peter", "address": "Lowstreet 27"}
result = mycol.insert_one(mydict)
print(result.inserted_id) # Will print the ID, an hex-like key value resembling "5b1910482ddb101b7042fcd7"

# If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
# For example:
#     mydict = {"_id": "10", "name": "Peter", "address": "Lowstreet 27"}
#     result = mycol.insert_one(mydict)
#     ... or...
#     db.Employee.insert({_id:10, "name" : "Peter", "address": "Lowstreet 27"})
# 
# In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).
