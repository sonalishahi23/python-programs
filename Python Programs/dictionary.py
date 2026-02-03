print("**********Marks**********")
name=input("Enter Your Name:- ")
marks= {
         "English" : input("Enter Marks in English:- "),
         "Hindi"   : input("Enter Marks in Hindi:- "),
         "Maths"   : input("Enter Marks in Maths:- "),
         "Science" : input("Enter Marks in Science:- "),
         "Computer": input("Enter Marks in Computer:- "),
        }
total= int(marks["English"]) + int(marks["Hindi"]) + int(marks["Maths"]) + int(marks["Science"]) +int(marks["Computer"])
percentage=float(total/500)*100

print("**********Marksheet**********")
print(f"Student name:- {name}")
print(f"Marks in English:- ",marks["English"])
print(f"Marks in Hindi:- ",marks["Hindi"])
print(f"Marks in Maths:- ",marks["Maths"])
print(f"Marks in Science:- ",marks["Science"])
print(f"Marks in Computer:- ",marks["Computer"])
print("Percentage is ", percentage)

