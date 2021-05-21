# Python_MongoDB_Query_06_filter_regex_0603.py
# 
# Python MongoDB Query
# 
# Filter With Regular Expressions
# ===============================
# You can also use regular expressions as a modifier.
# Regular expressions can only be used to query strings.
# 
# To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}.
# 
# Example: Find documents where the address starts with the letter "S"
# --------------------------------------------------------------------
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }

mydocs = mycoll.find(myquery)

for document in mydocs:
    print(document)

#### END ####
