name=input("Enter your Name:-")
print("Length of the Name is ",len(name))

full_name=input("Enter Your full name:- ")
if full_name.isalpha()==False:
    if full_name.count(" ")==1:
        print("Valid Name")
    else:
        print("Invalid Name")
else:
    print("Invalid name")


