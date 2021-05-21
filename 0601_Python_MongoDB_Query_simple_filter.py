# Python_MongoDB_Query_simple_filter_0601.py
# 
# Python MongoDB Query
# 
# Filter the Result:
# ==================
# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search.
# 
# Example: Find document(s) with the address "Rua das flores, 863"
# ----------------------------------------------------------------
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

myquery = { "address": "Rua das flores, 863" }

mydocs = mycoll.find(myquery)

for document in mydocs:
    print(document)

#### END ####
