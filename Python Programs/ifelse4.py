print("Checking Sum of 2 numbers lies between 1 and 1000 or not")
number={
    "number1" : int(input("Enter First Number: ")),
    "number2" : int(input("Enter Second Number: "))
}
sum = number["number1"] + number["number2"]
print("Sum is ",sum)
if sum>1:
    if sum<1000:
        print("The Number lies between 1 and 1000")
    else:
        print("The Number does not lies between 1 and 1000.")
else:
    print("The Number does not lies between 1 and 1000.")