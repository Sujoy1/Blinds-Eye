import pymongo
from pymongo import MongoClient
from connect_to_cloud import *

collection = connect_to_cloud()

results = collection.find({})
for x in results:
    print(x)