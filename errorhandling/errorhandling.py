num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
try:
    res=num1/num2
    print(res)

except Exception as e:
    print(e.args)

finally:
    print("line1")
    print("line2")