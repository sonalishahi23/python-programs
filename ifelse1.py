print(" ***Vote Eligiblity*** ")
data={
      "name": input("Enter Your Name: "),
      "gender" : input("Enter Your Gender: "),
      "age": int(input("Enter Your Age:- ")),
      "nationality" : input("Enter Your Nationality; ")

}
print(" ***Vote Eligiblity*** ")
print(f"Name of Candidate:- {data["name"]} ")
print(f"Gender of Candidate:- {data["gender"]} ")
print(f"Age of Candidate:- {data["age"]} ")
print(f"Nationality of Candidate:- {data["nationality"]} ")
if data["age"]>=18:
    print("User is Eligible to vote")
else:
    print("User is not Eligible to vote.")
