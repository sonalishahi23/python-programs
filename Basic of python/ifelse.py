print("**********Marks**********")
marks= {
         "English" : input("Enter Marks in English:- "),
         "Hindi"   : input("Enter Marks in Hindi:- "),
         "Maths"   : input("Enter Marks in Maths:- "),
         "Science" : input("Enter Marks in Science:- "),
        }
total= int(marks["English"]) + int(marks["Hindi"]) + int(marks["Maths"]) + int(marks["Science"])
percentage=total/4

print("**********Marksheet**********")
print(f"Marks in English:- ",marks["English"])
print(f"Marks in Hindi:- ",marks["Hindi"])
print(f"Marks in Maths:- ",marks["Maths"])
print(f"Marks in Science:- ",marks["Science"])
print(f"Total marks: {total}")
print("Percentage is ", percentage)
if percentage>=60:
    print("Pass")
else:
    print("Fail")

