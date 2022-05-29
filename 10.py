def square (num):
    result = num * num
    return result , num


a = square(4)
print(a)
square(10)


a = input("enter your age")
if 0 < a < 120:
    print ("ok")
else:
    print("not ok")

b = int(input("enter amount of pets: "))
    if 0 < b < 4:
        print("ok")

else:
    print("not ok")

def validate(prompt):
    input_from_user = int(input(prompt))
    if 0 < input_from_user < 120:
        print("ok")
    else:
        print("not ok")

validate("enter your age")

