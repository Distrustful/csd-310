#Code to connect to MongoDB
from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cybr410.y79aaov.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Find and display all results in student DB
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]) + "\n")

#update_one method (updating one document)
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Lies"}})

#Find and display one result in student DB
doc = db.students.find_one({"student_id": "1007"})

print("-- Displaying STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]))
