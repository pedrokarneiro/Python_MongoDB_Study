# Python MongoDB Sort
# 0702_Python_MongoDB_Sort_DESCending.py
#
# Sort the Result
# ===============
# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
# 
# Sort Descending
# ---------------
# Use the value -1 as the second parameter to sort descending.
# 
# sort("name", 1)  #ascending
# sort("name", -1) #descending
# 
# Example: Sort the result reverse alphabetically by name
 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycoll = mydb["customers"]

# sort("name")     #ASCending (default)
# sort("name", 1)  #ASCending
# sort("name", -1) #DESCending <-------- In this example
mydocs = mycoll.find().sort("name", -1)

for document in mydocs:
    print(document)
