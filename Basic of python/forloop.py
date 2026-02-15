dictdata=[
    {"id":101,"name":"Sonali","address":"Rohtak"},
    {"id":102,"name":"Riya","address":"Delhi"},
    {"id":103,"name":"Nitika","address":"Sonipat"}
    ]
user_enter_name=input("Please Enter Your Name: ")
found=False
for data in dictdata:
    if data["name"]==user_enter_name:
       print("Record is Found Successfully")
       found=True
       break
if not found:
    print("Record does not exists.")    
