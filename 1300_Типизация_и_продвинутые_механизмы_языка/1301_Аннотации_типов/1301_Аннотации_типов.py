"""
1301_Аннотации_типов
"""

def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))

name: str = 'Alice'
age: int = 30
salary: float = 50000.0

names: list[str] = ['Alice', 'Bob', 'Charlie']
users: dict[str, int] = {
    'Alice': 30, 
    'Bob': 25, 
    'Charlie': 35
}

value: int | str = 100

search_value: int | str = 'ноутбук'

phone_number: str | None = None
phone_number = '123-456-7890'


class User:
    name: str
    age: int
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        

user = User('Alice', 30)

class Product:
    title: str
    price: float
    quantity: int
    
    def __init__(
        self, 
        title: str, 
        price: float, 
        quantity: int
    ):
        self.title = title
        self.price = price
        self.quantity = quantity    
    
class User:
    def __init__(
        self, 
        name: str, 
        age: int, 
        email: str | None = None
    ):
        self.name = name
        self.age = age
        self.email = email
        
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str | None = None
    
    
user = User('Alice', 30, 'alice@example.com')
print(user)

type UserId = int

user_id: UserId = 12345

type ProductPrices = dict[str, float]

prices: ProductPrices = {
    'laptop': 999.99,
    'phone': 499.99,
}

def get_first(items: list):
    return items[0]

def get_first[T](items: list[T]) -> T: # def get_first[T](...)
    return items[0]

names = ['Alice', 'Bob', 'Charlie']
result = get_first(names)
print(result)

numbers = [10, 20, 30]
result = get_first(numbers)
print(result)

def get_first[ItemType](items: list[ItemType]) -> ItemType:
    return items[0]

"""
T
K
V
E
U

dict[K, V]
"""
def identity[T](value: T) -> T:
    return value

x = identity(42)

def make_pair[T, U](first: T, second: U) -> tuple[T, U]:
    return first, second

result = make_pair(42, "hello") # tuple[int, str]

class Box[T]:
    def __init__(self, value: T):
        self.value = value
        
        
name_box = Box[str]('Alice')
number_box = Box[int](42)


def get_last[T](items: list[T]) -> T:
    # print(T)
    return items[-1]
data = [1, 2, 3] # int
get_last(data)

"""
T
K
V
E
U
W
N
R
P
S
C
"""
def identity[T](value: T) -> T:
    return value

def pair[T, U](first: T, second: U) -> tuple[T, U]:
    return first, second

"""
i
j
k
l
"""

def example[T, U, V](x: T, y: U, z: V) -> tuple[T, U, V]:
    ...

class Container[T]:
    ...
    
class Container[E]:
    ...
    
# def wrapper[R](func: callable[..., R]) -> callable[..., R]:
#     ...
    
# def decorator[P, R](func: callable[P, R]) -> callable[P, R]:
#     ...


def convert[T, S](value: T) -> S:
    ...
    
class Repository[C]:
    ...
    
    


a: object = 42

class Animal:
    pass
class Dog(Animal):
    pass


list[Dog]

names: list[str] = ['Alice', 'Bob', 'Charlie']

name = names[0]
name.capitalize()

data: dict[str, list[int]]

numbers: list[int] = [1, 2, 3]
numbers.append('four')

