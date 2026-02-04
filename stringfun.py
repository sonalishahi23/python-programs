print("***** STUDENT EXAMINATION FORM *****")
information = {
    "name": input("Enter your Full Name: "),
    "class": input("Enter Your Class: "),
    "roll_no": input("Enter Roll Number: "),
    "course": input("Enter your Course Name: "),
    "email": input("Enter your E-mail: ")
}
print("***** STUDENT EXAMINATION FORM *****")
print(f"Student Name : {information["name"].title()}")
print(f"Class : {information["class"].isalnum()}")
print(f"Student Roll No. : {information["roll_no"].zfill(10)}")
print(f"Course Name : {information["course"].upper()}")
print(f"E-mail : {information["email"].lower()}")


print(f"Roll number is digit : {information["roll_no"].isdigit()}")
print(f"Name is on Centre: {information["name"].center(6,"*")}")
print(f"how many times a occurs in email: {information["email"].count("a")}")
print(f"Find the index of A in name: {information["name"].find("a")}")








