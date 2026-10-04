from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["Auth_project"]

collection = db["users"]

