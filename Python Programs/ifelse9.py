print("*****Mobile recharge validity check*****")
print("Recharge Amounts are:")
print("1. 199 rs")
print("2. 299 rs")
print("3. 399 rs")
amount =int(input("Enter recharge amount: "))
if amount == 199:
    print("Recharge successful")
    print("Validity: 28 days")
else:
    if amount == 249:
        print("Recharge successful")
        print("Validity: 30 days")
    else:
        if amount == 399:
            print("Recharge successful")
            print("Validity: 56 days")
        else:
            print("Invalid recharge plan")