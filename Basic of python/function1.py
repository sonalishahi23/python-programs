def user_input():
    data={
        "id" :input("Enter Student ID: "),
        "name" : input("Enter Student Name: ")
    }
    return data

def output():
    show=user_input()
    print(show)
    return 0


output()