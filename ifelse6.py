print("Checking a Triangle is valid or not")
sides={
    "side1": int(input("Enter First Side: ")),
    "side2": int(input("Enter Second Side: ")),
    "side3": int(input("Enter Third Side: "))
}
if sides["side1"]+sides["side2"]>sides["side3"]:
    if sides["side2"]+sides["side3"]>sides["side1"]:
        if sides["side1"]+sides["side3"]>sides["side2"]:
            print(" Triangle is Valid.")
        else:
            print("The triangle is not valid")
            print(" Sum of side1 and side3 is not greater than side2")
    else:
        print("The triangle is not valid")
        print(" Sum of side2 and side3 is not greater than side1")
else:
    print("The triangle is not valid")
    print(" Sum of side1 and side2 is not greater than side3")