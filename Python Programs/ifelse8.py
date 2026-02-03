print("***** Electricity bill Calculation*****")
units = int(input("Enter electricity units consumed: "))
if units <= 100:
    bill = units*2
    print("Electricity bill amount is:", bill)
else:
    if units <= 200:
        bill = units*3
        print("Electricity bill amount is:", bill)
    else:
        bill = units*5
        print("Electricity bill amount is:", bill)
