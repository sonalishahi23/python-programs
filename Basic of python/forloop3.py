print("Table of any number which user will enter")
user_input=int(input("Enter Any Number: "))
for i in range(1,11):
     print(user_input * i)

print("Sum of n natural numbers")
input=int(input("Enter any number: "))
sum=0
for n in range(1,input+1):
    sum+=n
print("Sum: ",sum)