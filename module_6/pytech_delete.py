#Code to connect to MongoDB
from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cybr410.y79aaov.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]

#Find and display all results in student DB
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]) + "\n")

#Insert new user into DB
ronald = {
    "student_id": "1010",
    "first_name": "Ronald",
    "last_name": "Mcdonald"
}

ronald_student_id = students.insert_one(ronald).inserted_id

print( "-- Insert Statements --")
print("Inserted student record Ronald Mcdonald into the students collection with document_id " + str(ronald_student_id) + "\n")

#Find and display one result in student DB (prove ronald got added)
doc = db.students.find_one({"student_id": "1010"})

print("-- Displaying STUDENT TEST DOC --")
print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]) + "\n")

#Delete ronald from DB
db.students.delete_one({"student_id": "1010"})

#Find and display all results in student DB (prove ronald is gone)
docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]) + "\n")



