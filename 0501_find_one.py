# 0501_find_one.py
# 
# Python MongoDB Find
# ===================
# 
# In MongoDB we use the find() and find_one() methods to find data in a collection
# just like the SELECT statement is used to find data in a table in a MySQL database.
# 
# Find One
# --------
# To select data from a collection in MongoDB, we can use the find_one() method.
# 
# The find_one() method returns the first occurrence in the selection.
# 
# Example
# Find the first document in the customers collection:
 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycollection = mydb["customers"]

x = mycollection.find_one()

print(x)
