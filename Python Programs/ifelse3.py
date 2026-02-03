print("***Login Portal***")
correct_username="sonali_123"
correct_password="Sonali@123"
data={
    "username" : input("Enter username: "),
    "password" : input("Enter password: ")
}
if data["username"]==correct_username:
    if data["password"]==correct_password:
        print("Login Successfully!!")
    else:
        print("Incorrect Password")
else:
    if data["password"] != correct_password:
        print("Login failed! Both username and password are incorrect.")
    else:
        print("Login failed! Incorrect username.")
    