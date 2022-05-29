my_file = open("names.txt", "w")
for i in range(5):
    current_name = input("enter your name: ")
    my_file.write(f"{current_name}\n")

my_file.close()

def your_name():
    my_file = open("names.txt", "w")
    for i in range(5):
        current_name = input("enter your name: ")
        my_file.write(f"{current_name}\n")

your_name()


def get_name():
    n = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{n}\n")

    def show_names():
        with open("names.txt") as my_file:
            for line in my_file.readlines():
                print(f"hello {line}", end='')


def call_urls():
    with open("urls.txt") as urls:
        for line in url.readlines():
            url_caller(line.strip())

call_urls()

