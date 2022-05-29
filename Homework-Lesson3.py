
if __name__ == '__main__':
    try:
        a = 1 / 0
    except:
        print("Division by zero")


  #3 , Yes


#4 all


# 5


# 6 # Except IO exceptions +  Except ZeroDivisionError



# 7:
Newfile = open("c:/ronny/words.txt",'w')
Newfile.close()

# 8
Newfile = open("c:/ronny/words.txt",'w')
Newfile.write("words")
Newfile.close()

# 9
Newfile = open("c:/ronny/words.txt",'r')
str = Newfile.read()a
print(str)
Newfile.close()

# 10
Newfile = open("c:/ronny/hebrew.txt",'w',encoding='utf-8')
Newfile.write"שלום")
Newfile.close()

my_file2 = open("c:/temp/hebrew.txt",'r',encoding='utf-8')
str = my_file2.read()
print(str)
