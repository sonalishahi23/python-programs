print("Finding Largest of 3 Numbers")
number={
    "number1" : int(input("Enter First Number: ")),
    "number2" : int(input("Enter Second Number: ")),
    "number3" : int(input("Enter Third Number: "))
}
if number["number1"]>number["number2"]:
    if number["number1"]>number["number3"]:
        print(f"Largest number is {number["number1"]}")
    else:
        print(f"Largest number is {number["number3"]}")
else:
    if number["number2"]>number["number3"]:
        print(f"Largest number is {number["number2"]}")
    else:
        print(f"Largest number is {number["number3"]}")