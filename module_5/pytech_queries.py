from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cybr410.y79aaov.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print(doc)

doc = db.students.find_one({"student_id": "1007"})

print("-- Displaying STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]))
