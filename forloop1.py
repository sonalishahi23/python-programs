user_input=int(input("Please Enter the number of Students you want to Register: "))
data=[]
if user_input<=0 or user_input>5:
    print("Please Choose a number between 1 to 5 as Maximum Limit is 5 only.")
else:
     for i in range(1,user_input+1):
         student={
             "details" :f"Student {i} details",
             "id" : int(input("Enter Student ID: ")),
             "name" : input("Enter Student Name: "),
             "address" : input("Enter Student Address: ")
         }
         data.append(student)
for i in range(len(data)):
    print(data[i]["details"])
    print("Student ID: ", data[i]["id"])
    print("Student Name: ",data[i]["name"])
    print("Student Address: ", data[i]["address"])
