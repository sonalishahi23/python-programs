x=int(input("Enter Value of x: "))
y=int(input("Enter Value of y: "))
def menu():
    print("Menu")
    print("1. Addition")
    print("2. Subtration")
    print("3. Multiply")
    choice=user_input()
    if choice==1:
        print("Sum is ",x+y )
    elif choice==2:
        print("subtraction is: ", x-y)
    elif choice==3:
        print("multiplication is: ",x*y)

def user_input():
    choice=int(input("Enter your choice: "))
    return choice

menu()