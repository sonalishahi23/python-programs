x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
def menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice=int(input("Please Choose any option: "))
    return choice

def add(x,y):
    print("Sum is ",x+y)

def sub (x,y):
    print("Subtraction is ",x-y)

def multiplication(x,y):
    print("Multiplication is ",x*y)

def division(x,y):
    print("Division is ",x/y)


def dashboard():
    choice=menu()
    if choice==1:
        add(x,y)
    elif choice==2:
        sub(x,y)
    elif choice==3:
        multiplication(x,y)
    elif choice==4:
        division(x,y)

dashboard()