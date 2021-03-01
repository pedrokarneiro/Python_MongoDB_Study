# 03 MongoDB Create Collection
# 03_MongoDB_Create_Collection.py
# 
# A collection in MongoDB is the same as a table in SQL databases.
# 
# Creating a Collection
# ---------------------
# 
# To create a collection in MongoDB, use the database object and specify the name of the collection you want to create.
# Mongo DB will create the collection if it does not exist.
# 
# Example:
# Create a collection called "customers":
# 
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# 
# Important: In MongoDB, a collection is not created until it gets content!
# 
# Check If Collection Exists
# --------------------------
# 
# Remember: in MongoDb, a collection is not created until it gets content, so if this is your first time creating a collection,
# you should complete the next chapter (create document) before you check if the collection actually exists!
# 
# you can check if a collection exists in a database by listing all collections.
# 
# Example:
# Return a list of all collections in your database:
# 
# print(mydb.list_collection_names())
# 
# Or you can check a specific collection by name:
# 
# Example:
# Check if the "customers" collection exists:
# 
# collist = mydb.list_collection_names()
# if "customers" in collist:
#    print("The collection exists.")


