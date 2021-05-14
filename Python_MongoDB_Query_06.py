# Python_MongoDB_Query_06.py
# 
# Python MongoDB Query
# 
# Filter the Result:
# ==================
# When finding documents in a collection, you can filter the result by using a query object.
# The first argument of the find() method is a query object, and is used to limit the search.
# 
# Example: Find document(s) with the address "Park Lane 38"
# ---------------------------------------------------------
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# myquery = { "address": "Park Lane 38" }
# 
# mydocs = mycoll.find(myquery)
# 
# for document in mydocs:
#   print(document)
# 
# #### END ####
# 
# Advanced Query
# ==============
# To make advanced queries you can use modifiers as values in the query object.
# E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}.
# More examples of modifiers at this code: https://gist.github.com/javierarilos/015e2ce27cecdea63564
# 
# Example: Find documents where the address starts with the letter "S" or higher
# ------------------------------------------------------------------------------
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# myquery = { "address": { "$gt": "S" } }
# 
# mydocs = mycoll.find(myquery)
# 
# for document in mydocs:
#   print(document)
# 
# #### END ####
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
# import pymongo
# 
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycoll = mydb["customers"]
# 
# myquery = { "address": { "$regex": "^S" } }
# 
# mydocs = mycoll.find(myquery)
# 
# for document in mydocs:
#   print(document)
# 
# #### END ####
