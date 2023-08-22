lst=[10,20,30,40,50]
location=int(input("enter the location to fetch value from list: "))

try:
    print(lst(location))
except Exception as e:
    location=int(input("enter the location to fetch value from list: "))
    try:
        print(lst(location))
    except Exception as e:
        print(e.args)

    
finally:
    print("dbcommit")
    print("file read")
