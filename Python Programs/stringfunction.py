student=[
    {
        "details" : "*****Student 1 Details*****",
        "id" : (input("Enter Student ID : ").zfill(18)),
        "name" : input("Enter Student Name : ").isalpha(),
        "address" : input("Enter Student Address: ").isalnum()
    },
    {
        "details" : "*****Student 2 Details*****",
        "id" : (input("Enter Student ID : ").zfill(18)),
        "name" : input("Enter Student Name : ").isalpha(),
        "address" : input("Enter Student Address: ").isalnum()
    }
]
print(student[0]["details"])
print("Student ID: ", student[0]["id"])

print("Student Name: ",student[0]["name"])
print("Student Address: ",student[0]["address"])

print(student[1]["details"])
print("Student ID: ", student[1]["id"])
print("Student Name: ",student[1]["name"])
print("Student address: ",student[1]["address"])