from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cybr410.y79aaov.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(" -- Pytech Collection List --")
print(db.list_collection_names())
