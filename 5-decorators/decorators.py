def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def hello():
    print("Hello")


@my_decorator
def bye():
    print("Bye")


hello()
bye()

my_decorator(hello)()  # This is the same as calling hello()
