def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('Hello')
