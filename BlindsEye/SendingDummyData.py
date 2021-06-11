import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://SujoySeal:bKWb09V1uBbMMhJb@post-boxcluster-sujoy.i9ean.mongodb.net/FYP-Database?retryWrites=true&w=majority")
db = cluster["FYP-Database"]
collection = db["Identified-Objects"]

post = { "name" : "Sujoy","Addrees":"Durgapur"}

collection.insert_one(post)


#mongodb+srv://<username>:<password>@post-boxcluster-sujoy.i9ean.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
