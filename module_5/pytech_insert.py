from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cybr410.y79aaov.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["students"]

taylor = {
    "student_id": "1007",
    "first_name": "Taylor",
    "last_name": "Damron"
}

john = {
    "student_id": "1008",
    "first_name": "John",
    "last_name": "Doe"
}

jane = {
    "student_id": "1009",
    "first_name": "Jane",
    "last_name": "Doe"
}


taylor_student_id = students.insert_one(taylor).inserted_id
john_student_id = students.insert_one(john).inserted_id
jane_student_id = students.insert_one(jane).inserted_id

print( "-- Insert Statements --")
print("Inserted student record Taylor Damron into the students collection with document_id " + str(taylor_student_id))
print("Inserted student record John Doe into the students collection with document_id " + str(john_student_id))
print("Inserted student record Jane Doe into the students collection with document_id " + str(jane_student_id))