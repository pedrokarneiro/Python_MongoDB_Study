# Python MongoDB Sort
# 0701_Python_MongoDB_Sort_ASCending.py
#
# Sort the Result
# ===============
# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
# 
# Example: Sort the result alphabetically by name

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

# sort("name")     #ASCending (default) <-------- In this example
# sort("name", 1)  #ASCending
# sort("name", -1) #DESCending
mydocs = mycoll.find().sort("name")

for document in mydocs:
    print(document)


