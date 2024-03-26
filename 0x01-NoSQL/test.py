from pymongo import MongoClient
client = MongoClient()

dbases = client.list_database_names()

print(dbases)