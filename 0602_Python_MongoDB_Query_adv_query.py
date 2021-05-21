# Python_MongoDB_Query_adv_query_0602.py
# 
# Python MongoDB Query
# 
# Advanced Query
# ==============
# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}.
# More examples of modifiers at this code: https://gist.github.com/javierarilos/015e2ce27cecdea63564
# 
# Example: Find documents where the address starts with the letter "S" or higher
# ------------------------------------------------------------------------------
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

myquery = { "address": { "$gt": "S" } }

mydocs = mycoll.find(myquery)

for document in mydocs:
    print(document)

#### END ####
