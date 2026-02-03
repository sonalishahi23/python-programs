print("*****Movie ticket calculater*****")
print("Seats are:")
print("1. Silver")
print("2. Gold")
print("3. Daimond")
data={
      "seat" : input("Enter seat which you want to choose: "),
      "tickets" : int(input("Enter number of tickets: "))
}
if data["seat"] == "Silver":
    total = data["tickets"] * 150
    print("Seat Type: Silver")
    print("Total Amount:", total)
else:
    if data["seat"] == "Gold":
        total = data["tickets"] * 250
        print("Seat Type: Gold")
        print("Total Amount:", total)
    else:
        if data["seat"] == "Diamond":
            total = data["tickets"] * 400
            print("Seat Type: Premium")
            print("Total Amount:", total)
        else:
            print("Invalid seat type")



