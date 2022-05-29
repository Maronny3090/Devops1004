try:
    a = int(input("enter first number:"))
    b = (int(input("enter second number: ")))
    print(a/b)
except ZeroDivisionError:
    print("could not divide by zero")
except FileNotFoundError:
        print("could not find file")
except Exception as e:
    print(e.args)
    print("bla")


#import requests
#requests.get("http://www.google.com")
