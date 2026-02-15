import json

data=[]

for i in range(1,3):
    student={
             "details"  :f"Student {i} details",
             "id"       : int(input("Enter Student ID: ")),
             "name"     : input("Enter Student Name: "),
             "address"  : input("Enter Student Address: ")
        }
    data.append(student)
print(json.dumps(data,indent=4))