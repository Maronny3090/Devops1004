from datetime import datetime
def my_decorator(func):
    def wrapper():
        print(datetime.now())
        func()
        print(datetime.now())
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

@my_decorator
def say_bark():
    print("Woooooof!")

# say_whee = my_decorator(say_whee)
say_whee()
say_bark()