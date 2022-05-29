a = "hello world"
my_names = ["adi","ben","noam","arthur","ron"]

for i in range (1,6):
        print(f"hello world")

for name in my_names:
        print(f"hello {name}")
    if name == "arhtur":
        break
else:
    print("prineted all names")
for i in range(len(my_names)):
    print(my_names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1

l = []
current_input = input("enter letter:")
while current_input != "q":
    l.append(current_input)
    current_input = input ("enter letter:")

print(f"inputs are {l}")


a = 0
while a < 5:
    print(a)
    if a == 2:
        break

        a = a + 1



n = [1, 2, 3, 4, 5]

result = [num * 2 for num in n]
print (result)