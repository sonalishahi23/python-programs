print("ATM Money Withdrawl")
data={
    "balance" : int(input("Enter your account balance: ")),
    "amount" : int(input("Enter withdrawal amount: "))
}
if data["amount"] > 0:
    if data["amount"] <= data["balance"]:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Invalid withdrawal amount")