information={
        "id" : int(input("Enter Student ID : ")),
        "name" : input("Enter Student Name : "),
        "qualification" : input("Enter Student Qualification: "),
        "address" : input("Enter Your Address: ")
}
information["email"]=input("Enter Your Email: ")
print(information)
information.pop("address")
print(information)
