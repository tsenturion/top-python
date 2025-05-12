def greet(name):
    return f"hi, {name}"

say_hello = greet

print(say_hello('me'))


def to_uppder(string: str):
    return string.upper()

def print_formatted(formatter, message):
    print(formatter(message))

print_formatted(to_uppder, 'hi')


def outer(text):
    def inner():
        print(f"внутри {text}")
    return inner

func = outer('hi')
func()


def say_hi():
    print('hi')


def wrapper():
    print('вызывается функция say_hi')
    say_hi()

wrapper()


def wrapper(func):
    def inner(*args, **kwargs):
        print('до вызова')
        result = func(*args, **kwargs)
        print('после вызова')
        return result
    return inner

def say_hello():
    print("hi")


def decorator(func):
    def wrapper():
        print('функция вызывается')
        func()
    return wrapper

say_hello = decorator(say_hello)

@decorator
def say_hello():
    print("привет")