age=int(input("enter the age: "))

if age<18:
    raise Exception("invalid age")
else:
    print("valid")
