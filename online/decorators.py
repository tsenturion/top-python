"""def decorator(func):
    def wrapper():
        print("декоратор сработал до вызова функции")
        func()
        print("после вызова")
    return wrapper

@decorator
def say_hello():
    print('функция')

say_hello()"""
from pandas.compat.numpy.function import validate_argsort

"""def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"вызывается {func.__name__} с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"функция {func.__name__} завершила выполнение")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 5))"""
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print('hi')

say_hi()"""

"""def methor_decorator(func):
    def wrapper(self, *args, **kwargs):
        print(f"вызов метода {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Example:
    @methor_decorator
    def greet(self):
        print("привет от класса")

obj = Example()
obj.greet()
"""
"""from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("выполняетя декорированная функция")
        return func(*args, **kwargs)
    return wrapper

@decorator
def example():
    """"""эта функция возвращает hello""""""
    return "hello"

print(example.__name__)
print(example.__doc__)"""
"""
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))

class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
Counter.increment()
print(Counter.count)

""""""
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("")
        self._radius = value

    @radius.deleter
    def radius(self):
        raise AttributeError("")



c = Circle(5)
print(c.radius)
#c.radius = -3
del c.radius"""

"""from functools import lru_cache

class Fibonacci:
    @lru_cache(maxsize=None)
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

f = Fibonacci()
print(f.fib(50))

from contextlib import contextmanager

class FileHandler:
    @contextmanager
    def open_file(self, filename):
        file = open(filename, 'w')
        try:
            yield file
        finally:
            file.close()

handler = FileHandler()
with handler.open_file("test.txt") as f:
    f.write("hi")



from functools import singledispatchmethod

class Printer:
    @singledispatchmethod
    def show(self, value):
        raise NotImplementedError("")

    @show.register
    def _(self, value: int):
        print(f"целое число: {value}")

    @show.register
    def _(self, value: str):
        print(f"строка {value}")

printer = Printer()
printer.show(10)
printer.show("hi")

from functools import  cached_property

class ExpensiveComputation:
    def __init__(self, x):
        self.x = x

    @cached_property
    def compute(self):
        print("выполнение сложных вычислений")
        return self.x ** 2

obj = ExpensiveComputation(10)
print(obj.compute)
print(obj.compute)


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(10, 20)
p2 = Point(10, 20)
print(p1)
print(p1 == p2)"""

from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

s1 = Student("q", 90)
s2 = Student("b", 85)

print(s1 > s2)
print(s1 <= s2)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return  get_instance

@singleton
class Database:
    def __init__(self):
        print("создали")

db1 = Database()
db2 = Database()

print(db1 is db2)


@classproperty
"""
аналог @propertry для класса

"""



@timing

@validate_args

@log_methods

