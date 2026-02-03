student=[
    {
        "details" : "*****Student 1 Details*****",
        "id" : int(input("Enter Student ID : ")),
        "name" : input("Enter Student Name : "),
        "qualification" : {
            "degree" : input("Enter Your Qualification Degree:- "),
            "Year"   : input("Enter Your Passing Year: ")
        },
        "email" :input("Enter Your Email:- ")
    },
    {
        "details" : "*****Student 2 Details*****",
        "id" : int(input("Enter Student ID : ")),
        "name" : input("Enter Student Name : "),
        "qualification" : {
            "degree" : input("Enter Your Qualification Degree:- "),
            "Year"   : input("Enter Your Passing Year: ")
        },
        "email" :input("Enter Your Email:- ")
    },
    {
        "details" : "*****Student 3 Details*****",
        "id" : int(input("Enter Student ID : ")),
        "name" : input("Enter Student Name : "),
        "qualification" : {
            "degree" : input("Enter Your Qualification Degree:- "),
            "Year"   : input("Enter Your Passing Year: ")
        },
        "email" :input("Enter Your Email:- ")
    }
]

print(student[0]["details"])
print("Student ID: ", student[0]["id"])
print("Student Name: ",student[0]["name"])
print("Student Qualification degree: ",student[0]["qualification"]["degree"])
print("Student  Qualification Passing Year:  ",student[0]["qualification"]["Year"])
print("Student Email: ",student[0]["email"])

print(student[1]["details"])
print("Student ID: ", student[1]["id"])
print("Student Name: ",student[1]["name"])
print("Student Qualification: ",student[1]["qualification"]["degree"])
print("Student  Qualification Passing Year:  ",student[1]["qualification"]["Year"])
print("Student Email: ",student[1]["email"])

print(student[2]["details"])
print("Student ID: ", student[2]["id"])
print("Student Name: ",student[2]["name"])
print("Student Qualification: ",student[2]["qualification"]["degree"])
print("Student  Qualification Passing Year:  ",student[2]["qualification"]["Year"])
print("Student Email: ",student[2]["email"])


