"""from time import *
print(pow(2, 3))
from math import pow
"""
import time
from typing import final

"""print(1, 2, 3, 4, '123' + '123', 5 % 2, 5 // 2, 2 ** 3)
number = input()  # ввод str с консоли
number = bool(number)
print(number)  # вывод в консоль
"""
"""
str   строки "123" '123'
int   целые числа 123 34554435435 35 53 534 53 334 345 53 453 345 43
float дробные 123.3 5.4 6.0
bool  булевы True/1 False/0
list список (не массив, но похож)
перевод в другое тип
str()
int()
float()
bool()

>
<
>=
<=
==
!=
and и/умножение
or или/сложение
not отрицание
"""
"""flag = 5 > 2 and 4 < 3 or True

if 5 > 2:
    print("правда")
else:
    print("ложь")

if flag:
    print("правда")
else:
    print("ложь")
    """
"""if False:
    print()
elif False:
    print()
elif False:
    print()

if True:
    print()
start = time()
end = time()
while end - start < 1:
    end = time()
    print(1)
else:
    print('цикл закончился')
"""
"""str1 = '123456789'
for index, element in enumerate(str1):
    print(index, element)"""

"""for i in range(0, 51, 2):
    print(i)"""
"""
for _ in range(5):
    print('hi')

str1 = '123456789'
print(str1[::-1])  # перевернуть строку

str1 = '123456789'
print(str1[2:5])

list1 = []
list2 = [123, 345, 6, True, 'sdc']
list3 = list(range(5))
print(list3)
print(range(5))

for e in list3:
    if e % 2 == 0:
        print(e)

chetnie = [i for i in list3 if i % 2 == 0]
b = None
print(type(b).__name__)
print(chetnie)"""
"""
length = int(input())
list1 = []
for _ in range(length):
    list1.append(int(input()))

for index, element in enumerate(list1):
    print(index, element)

print(f'длина: {length}\nсписок: {list1}')"""

"""
chr() символ по юникод коду
hex() 16x
len() длина 
abs() модуль
max()
min()
sum()

in
"""

"""print(chr(65))
print(chr(97))

print(hex(255))"""
"""
str1 = '1234'
str2 = '235'"""
"""list1 = list(range(5))
print(len(str1), len(list1))
print(1, abs(-1))

print(max(list1), min(list1), sum(list1))"""
"""for c in str2:
    if c not in str1:
        print(c)"""

"""
console.log(Math.round(num)); //до ближайшего целого
console.log(Math.floor(num)); //округление вниз до ближайшего целого
console.log(Math.ceil(num)); //вверх до ближайшего целого
console.log(Math.trunc(num)); //убрать дробную часть
console.log(num.toFixed(2)); //определенное количество знаков после запятой"""

"""import math
from math import *
from math import pi, ceil, trunc, floor"""
"""
import math as m
from math import *
from math import pi as p, ceil as c, trunc, floor

print(list1)
print(custom_add(1, 2))

print(m.pi)
print(round(pi))
print(round(pi, 2))
print(f'{pi:.3}')
print(ceil(pi))
print(trunc(pi))
print(floor(pi))

print(c(p))
"""
"""import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from offline.main import list1
print(list1)"""

"""
12
12
"""
'''
34
34
'''
# 213
# 123

"""x = None
if x is None:
    print(True)"""

"""x = Null было раньше
x = Nil в go
"""

"""list1 = [False, True, False]
if any(list1):
    print(True)
list1 = [True, True, True]
if all(list1):
    print(True)
"""
""""x = 8 if 5 > 2 else 5
"""""""значение если правда условие значение если ложь"""
"""print(x)
"""
"""number = 0
match number:
    case 0:
        print(0)
    case 2:
        print(2)
    case _:
        print('другое число')
number = str(number)
match number:
    case int():
        print('int')
    case str():
        print('str')
    case _:
        print('другой тип')
tuple1 = 2, 3

match tuple1:
    case (0, 0):
        print('начало координат')
    case (2, 3):
        print(f'точка {tuple1}')
    case _:
        print('другая точка')
list1 = [1, 2, 3]
match list1:
    case []:
        print(None)
    case [1, 2, 3]:
        print(list1)
    case _:
        print("other")

"""
"""для js
loop1: for(,,)
    loop2: for(,,)
        break loop2"""
"""
for i in range(5):
    if i == 1:
        print(f'прерывание {i}')
        continue
    print(i)
    if i == 2:
        print(f'остановка {i}')
        break

str1 = '123'"""
"""print('frffr', 'ererferfer', 'erfr')
print()
print()
print('frffr', 'ererferfer', 'erfr', sep='0123')
print('frffr', 'ererferfer', 'erfr', sep='\t')
print('frffr', 'ererferfer', 'erfr', sep=' ')
print('frffr', 'ererferfer', 'erfr', sep='??')
print('frffr', 'ererferfer', 'erfr', end='\n')
print('frffr', 'ererferfer', 'erfr', end='\t')
print('frffr', 'ererferfer', 'erfr', end=' ')
print('frffr', 'ererferfer', 'erfr', end='??')
"""
"""def custom_add_print(a, b):
    print(a + b)

def custom_add_return(a, b):
    return a + b

def get_user_info():
    name = "matvey"
    age = 23
    return name, age

myName, myAge = get_user_info()
print(myAge, myName)

custom_add_print(1, 2)
a = custom_add_return(1, 2)
print(a)


list1 = []
list2 = [1, 2, {234, 234, 12}, (123, 32), '1231', [123, 123, 123]]
for i in range(2, 10, 2):
    list1.append(i)
    print(i)

print(list1)
for i in list1:
    print(i)

print(list1[-1])
print(list1.pop())
"""
"""# lst = [int(s) for s in input().split()]
list1 = [i for i in range(5)]
print(list1)
list1 = list(range(5))
print(list1)
list1 = [i ** 4 if i % 4 == 0 else i ** 2 for i in range(10) if i % 2 == 0]
print(list1)
list1 = [i * j for i in range(5) for j in range(5)]
print(list1)
list1 = [[i * j for i in range(5)] for j in range(5)]
print(list1)

# квадраты чисел от 3 до 50 с шагом 7
list1 = [i * i for i in range(3, 50, 7)]

# создать список четных чисел от 0 до 20
list1 = [i for i in range(20) if i % 2 == 0]

list2 = ['123', '123', '123', '123', '123f', '1234']
# создать список слов, длина которых больше 3
list2 = [word for word in list2 if len(word) > 3]
print(list2)
list3 = [1, 2, 3]
list4 = [100, 1000]
# создать список со всеми возможными суммами двух элементов из двух списков
list1 = [i + j for i in list3 for j in list4]
print(list1)
"""
"""
try:
    a = float(input())
    b = float(input())
    print(a / b)

except ZeroDivisionError:
    print("нельзя / на 0")
except ValueError:
    print("введено не число")

except Exception as ex:
    print(ex)
    print("неизвестная ошибка")

else:
    print('ошибок не возникло')
finally:
    print("тест завершен")"""

"""
вводим а б
попробуем поделить а на б
ZeroDivisionError если делим на 0. печать нельзя на 0
ValueError если не число. печать введено не число
в остальных случаях печать неизвестная ошибка
"""

"""def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))"""


"""def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())
print(counter1())
print(counter1())"""
"""
функция умножения
"""
"""def make_multiplier(x):
    def inner_function(y):
        return x * y
    return inner_function

times3 = make_multiplier(3)
print(times3(9)) # 27
print(times3(9)) # 27

def outer_function(name):
    return lambda: f'Hello, {name}'

greet = outer_function('alice')
print(greet())
greet = outer_function('112')
print(greet())

multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y : x * y)

m1, m2, m3 = multipliers
print(m1(10))
print(m2(10))
print(m3(10))

multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y, real_x=x : real_x * y)

m1, m2, m3 = multipliers
print(m1(10))
print(m2(10))
print(m3(10))
"""
"""def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter"""
"""def make_counter():
    count = [0]
    return lambda: (count.append(count[-1] + 1) or count[-1])

# 1 счетчик
counter1 = make_counter()
print(counter1()) # 1
print(counter1()) # 2
print(counter1()) # 3

def make_multiplier(n):
    return lambda x : x * n
# умножение на число. Принимает число, возвращает замыкание
times5 = make_multiplier(5)
print(times5(10)) # 50
print(times5(3)) # 15

def filter_by_threshold(threshold):
    return lambda numbers: [n for n in numbers if n > threshold]
# фильтрация списка. Принимает пороговое значение, возвращает замыкание для фильтрации списка чисел
filter_above_10 = filter_by_threshold(10)
print(filter_above_10([5, 10, 15, 20])) # [15, 20]

def create_functions(numbers):
    return [lambda x, n=n: x * n for n in numbers]
# создание множества функций. Принимает список чисел, возвращает список функций. Кажая функция умножает входное на соответствующее из списка
functions = create_functions([2, 3, 4])
print(functions[0](10)) # 20
print(functions[1](10)) # 30
print(functions[2](10)) # 40"""

"""def count_up_to(max1):
    count = 1
    while count <= max1:
        yield count
        count += 1

list1 = list(count_up_to(3))
print(list1)
for number in count_up_to(3):
    print(number)
# ----------------------------------------------------------------

def get_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i

list_of_nums = [1, 2, 3, 8, 15, 42]
for i in get_even(list_of_nums):
    print(i, end=' ')

print()
# ----------------------------------------------------------------

def nextCube():
    acc = 1
    while True:
        yield acc ** 3
        acc += 1

count = 1
for num in nextCube():
    if count > 15:
        break
    print(num)
    count += 1

# ----------------------------------------------------------------

str1 = '1234589'
iter1 = iter(str1)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
# ----------------------------------------------------------------

list1 = [1, 2, 3]
iter2 = iter(list1)
try:
    print(next(iter2))
    print(next(iter2))
    print(next(iter2))
    print(next(iter2))
except StopIteration:
    print('конец')
# ----------------------------------------------------------------

def number_generator():
    for i in range(1, 6):
        yield i

gen = number_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# ----------------------------------------------------------------

import random

def random_number_generator():
    while True:
        yield random.randint(1, 100)

gen = random_number_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# ----------------------------------------------------------------

# фибоначчи

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
# ----------------------------------------------------------------

from itertools import chain, cycle, count

combined = list(chain(iter([1, 2]), iter(['a', 'b'])))
print(combined)
# ----------------------------------------------------------------
cyclic_iterator = cycle([10, 20, 50])
for i in range(20):
    print(next(cyclic_iterator), end=' ')
# ----------------------------------------------------------------

for i in count(10):
    if i > 15:
        break
    print(i)

# ----------------------------------------------------------------"""

"""f(a, b, c) => result
f(a)(b)(c) => result"""
"""
def add(a, b):
    return  a + b

def add_curried(a):
    def inner(b):
        return a + b
    return inner

result = add_curried(5)(10)
print(result)

add_five = add_curried(5)
print(add_five(10))
print(add_five(20))
# ----------------------------------------------------------------
def multiply(a):
    def inner(b):
        def inner2(c):
            return a * b * c
        return inner2
    return inner

result = multiply(2)(3)(4)
print(result)
# ----------------------------------------------------------------
from functools import partial

def add2(a, b, c):
    return a + b + c

add_five = partial(add2, 5)
result = add_five(10, 15)

print(result)
# ----------------------------------------------------------------

def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args : curried(*(args + more_args))
    return curried

@curry
def add(a, b, c):
    return a + b + c

result = add(5)(10)(15)
print(result)
# ----------------------------------------------------------------
@curry
def filter_list(predicate, lst):
    return list(filter(predicate, lst))

filter_even = filter_list(lambda x : x % 2 == 0)
result = filter_even([1, 2, 3, 4, 5])
print(result)
# ----------------------------------------------------------------

@curry
def map_list(func, lst):
    return list(map(func, lst))

multiply_by_two = map_list(lambda x : x * 2)
result = multiply_by_two([1, 2, 3])
print(result)

# ----------------------------------------------------------------
def power(base, exponent):
    return base ** exponent

square = partial(power, 2)
print(square(3))
print(square(4))
# ----------------------------------------------------------------

def greet(greeting, name, punctuation):
    return f"{greeting}, {name}{punctuation}"

say_hello = partial(greet, "hello", punctuation='!')
print(say_hello("alice"))
print(say_hello("bob"))
# ----------------------------------------------------------------
def filter_greater_than(threshold, value):
    return value > threshold

filter_above_five = partial(filter_greater_than, 5)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered = list(filter(filter_above_five, numbers))
print(filtered)
# ----------------------------------------------------------------
def multiply(a, b):
    return a * b
multiply_by_three = partial(multiply, 3)
numbers = [1, 2, 3, 4]
result = list(map(multiply_by_three, numbers))
print(result)
# ----------------------------------------------------------------
def sort_by_key(key, items):
    return sorted(items, key=key)

sort_by_length = partial(sort_by_key, len)
words = ['123', '12345', '1234']
sorted_words = sort_by_length(words)
print(sorted_words)
# ----------------------------------------------------------------
def greet(name, greeting='hello', punctuation='!'):
    return f"{greeting}, {name}{punctuation}"

say_hi = partial(greet, greeting='hi', punctuation='.')
print(say_hi("alice"))
print(greet("alice"))
# ----------------------------------------------------------------
multiply_by_two = partial(map, lambda x : x * 2)
filter_even = partial(filter, lambda x : x % 2 == 0)

numbers = [1, 2, 3, 4, 5]
result = list(multiply_by_two(filter_even(numbers)))
print(result)
# ----------------------------------------------------------------
# принимает порог и список чисел, возвращает список чисел больших этого порога, с lambda; без partial; без @curry
def filter_greater_than(threshold):
    def inner(numbers):
        return list(filter(lambda x : x > threshold, numbers))
    return inner
# factor - множитель; и список чисел, возвращает список чисел умноженных на множитель, с lambda; без partial; без @curry
def map_multiply_by(factor):
    def inner(numbers):
        return list(map(lambda x: x * factor, numbers))
    return inner
# принимает приветствие, имя, знак, возвращает return f"{greeting}, {name}{punctuation}" без lambda; без partial; без @curry
def greet(greeting):
    def inner(name):
        def inner2(punctuation):
            return f"{greeting}, {name}{punctuation}"
        return inner2
    return inner

# Каррированная math_operator, принимает operator и два числа. Возвращает результат операции

def math_operator(operator):
    def inner1(a):
        def inner2(b):
            if operator == 'add':
                return a + b
            elif operator == 'subtract':
                return a - b
            elif operator == 'divide':
                if b == 0:
                    raise ZeroDivisionError('b == 0')
                else:
                    return a / b
            elif operator == 'multiply':
                return a * b
            else:
                raise ValueError('неизвестна ')
        return inner2
    return inner1
"""
"""
def func():
    x = 10
    print(x)

func()
# print(x)
# ----------------------------------------------------------------
x = 10

def func():
    print(x)

func()
# ----------------------------------------------------------------
x = 10

def func():
    global x
    x = 20

func()
print(x)
# ----------------------------------------------------------------
def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()
# ----------------------------------------------------------------
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print(x)

    inner()
    print(x)
outer()
# ----------------------------------------------------------------
print((len('123')))
"""
"""
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_2 = make_multiplier(2)
print(multiply_by_2(5))


def outer():
    x = 10
    def inner():
        return x
    return inner
func = outer()
print(func)"""


"""# Каррированная math_operator, принимает operator и два числа. Возвращает результат операции

def math_operator(operator):
    def inner1(a):
        def inner2(b):
            if operator == 'add':
                return a + b
            elif operator == 'subtract':
                return a - b
            elif operator == 'divide':
                if b == 0:
                    raise ZeroDivisionError('b == 0')
                else:
                    return a / b
            elif operator == 'multiply':
                return a * b
            else:
                raise ValueError('неизвестна ')
        return inner2
    return inner1


add = math_operator('add')
subtract = math_operator('subtract')
divide = math_operator('divide')
multiply = math_operator('multiply')

print(add(2)(5))
print(subtract(2)(5))
print(divide(2)(5))
print(multiply(2)(5))
"""

"""def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
print(c())
print(c())"""

"""def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expensive_computation(x):
    print('computing', end=' ')
    return x * x

print(expensive_computation(4))
print(expensive_computation(4))
"""
# create_counter - фабрика функций, тк есть increment, reset, decrement создает счетчик. Счетчик на +1, сохранение состояния - замыкание
# метод reset будет сбрасывать счетчик
# decrement уменьшает
"""
def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def reset():
        nonlocal count
        count = 0

    return counter, decrement, reset

counter, decrement, reset = create_counter()

print(counter())
print(counter())
print(decrement())
print(decrement())
print(counter())
reset()
print(counter())
"""
"""
Задание: Создать систему для отслеживания и управления счетчиком
Функция должна быть каррированной, то есть принимать несколько аргументов по частям.
Использовать замыкания для отслеживания состояния счетчика.
Применить partial для частичного применения функции.
Функция должна принимать переменное количество аргументов (например, добавление множества значений к счетчику).
Функция должна иметь побочные эффекты (например, вывод в консоль).
"""

"""def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40, 50))
print(sum_all())"""

"""def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='alice', age=30, job='student')"""

"""def display_info(name=None, *args, **kwargs):
    print(f"name: {name}")
    print(f"additional:")
    for arg in args:
        print(f'-{arg}')
    print("details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info('alice', 25, 'student', location='new york', houbbies='programming')"""
"""
def greet(greeting, *names, **options):
    print(greeting)
    for name in names:
        print(f'hello, {name}')
    if 'punctuatioin' in options:
        print(options['punctuatioin'])
    else:
        print('!')

greet('доброе утро', 'alice', 'bob', punctuatioin='!!!')


fruits = ('1', '2', '3', '4', '5', '5')
fruit_name = input()
print(fruits.count(fruit_name))
# ----------------------------------------------------------------
print(sum(fruit_name in fruit for fruit in fruits))
# ----------------------------------------------------------------
car_brands = ('123', '1234', '12345')
brand_to_replace = input()
replacement_word = input()
new_car_brands = tuple(replacement_word if brand == brand_to_replace else brand for brand in car_brands)
# result = tuple(map(lambda x : to_replace if x == title else x, data))
print(new_car_brands)


# ----------------------------------------------------------------
dictionary = {}

def add_word():
    eng = input()
    fch = input()
    dictionary[eng] = fch

def del_word():
    eng = input()
    if eng in dictionary:
        del dictionary[eng]
    else:
        raise Exception('')

def find_word():
    eng = input()
    if eng in dictionary:
        print(eng, dictionary[eng])
    else:
        print(None)

def update_word():
    eng = input()
    if eng in dictionary:
        fch = input()
        dictionary[eng] = fch
    else:
        print(None)

# ----------------------------------------------------------------
employees = {}

def add_employee():
    name = input()
    phone = input()
    email = input()
    position = input()
    office = input()
    skype = input()

    employees[name] = {
        "Телефон": phone,
        "Email": email,
        'Должность': position,
        "Кабинет": office,
        'Skype': skype
    }

def del_emp():
    name = input()
    if name in employees:
        del employees[name]
    else:
        raise Exception("")

def find_emp():
    name = input()
    if name in employees:
        for key, value in employees[name].items():
            print(f"{key}, {value}")
    else:
        print(None)

def update_emp():
    name = input()
    if name in employees:
        phone = input()
        email = input()
        position = input()
        office = input()
        skype = input()

        employees[name] = {
            "Телефон": phone,
            "Email": email,
            'Должность': position,
            "Кабинет": office,
            'Skype': skype
        }
    else:
        raise Exception("")

# ----------------------------------------------------------------

book_collectioin = {}

def add_book():
    author = input()
    title = input()
    genre = input()
    year = input()
    pages = input()
    publisher = input()

    book_collectioin[title] = {
        "Автор": author,
        'Жанр': genre,
        "Год выпуска": year,
        "Количество страниц": pages,
        "Издательство": publisher
    }"""
"""class Person:

    health = 100

    @classmethod
    def print_health(cls):
        print(cls.health)

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.__gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

Matvey = Person('name', 18, is_student=True)
Matvey2 = Person('name', 18)
Matvey2 = Person('name', 18)
print(Matvey.is_student)
Matvey.invert_is_student()
print(Matvey.is_student)
Matvey.to_learn()

Person.print_health()
print(Person.health)"""
"""
class A:
    @classmethod
    def df(cls):
        print(1)
    pass

class B(A):
    @classmethod
    def df(cls):
        print(1)
    pass

class C1(B):
    pass

class C2(B):
    @classmethod
    def df(cls):
        print(1)

class D(C1, C2):
    pass


D.df()
print(D.mro())"""

"""
адание 1 Реализуйте класс «Человек». Необходимо хранить в поляхкласса:ФИО,датурождения,контактныйтелефон, город, 
страну,домашнийадрес.Реализуйтеметодыкласса для ввода данных, вывода данных, реализуйте доступ к отдельным полям
 через методы класса."""
"""
class Person:
    def __init__(self, name=None, date=None, phone=None, town=None, country=None, address=None):
        self.__name = name
        self.__date = date
        self.__phone = phone
        self.__town = town
        self.__country = country
        self.__address = address

    def inp(self):
        self.__name = input()
        self.__date = input()
        self.__phone = input()
        self.__town = input()
        self.__country = input()
        self.__address = input()

    def prnt(self):
        print(self.__name, self.__date, self.__phone, self.__town, self.__country, self.__address)
        
    def get_name(self):
        return self.__name"""

"""class A:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def print_first(self):
        print(self.first)

class B(A):
    def __init__(self, first, second, third):
        super().__init__(first, second)
        self.third = third

    def bprint(self):
        super().print_first()
        """
#super(класс, объект)
"""
class A:
    def method(self):
        print('А')

    def greet(self):
        return "привет из A"

    def greet2(self):
        return "привет из A"

class B(A):
    def method(self):
        print("B")
        super(B, self).method()

    def greet(self):
        return super().greet() + "и привет из B"

    def greet2(self):
        return super().greet()
b = B()
b.method()


class LoggingMixin:
    def log(self, message):
        print(f"лог: {message}")

class DataProcessor(LoggingMixin):
    def process(self, data):
        self.log("обработка данных")
        return data.upper()

processor = DataProcessor()
print(processor.process("hello"))"""

"""Задание 3 Создать базовыйкласс«Домашнееживотное»ипро изводныеклассы
«Собака»,«Кошка»,«Попугай»,«Хомяк». 
Спомощью конструктора установить имя каждого жи вотного и его характеристики. 
Реализуйте для каждого из классов методы: 
■ Sound — издает звук животного (пишем текстом в консоль); 
■ Show — отображает имя животного; 
■ Type — отображает название его подвида;"""
"""
from abc import ABC, abstractmethod

class HomeAnimal(ABC):
    @abstractmethod
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    def show(self):
        print(f"имя: {self.name}")

    def type(self):
        print(f"Вид: {self.species}")

class Cat(HomeAnimal):
    def __init__(self, name):
        super().__init__(name, 'Cat')

    def sound(self):
        print('Cat')

class Dog(HomeAnimal):
    def __init__(self, name):
        super().__init__(name, 'Dog')

    def sound(self):
        print('Dog')

class Parrot(HomeAnimal):
    def __init__(self, name):
        super().__init__(name, 'Parrot')

    def sound(self):
        print('Parrot')

class Hamster(HomeAnimal):
    def __init__(self, name):
        super().__init__(name, 'Hamster')

    def sound(self):
        print('Hamster')

class A:
    def __init__(self):
        self.__hidden = 'secret'

    def get_hidden(self):
        return self.__hidden

a = A()
print(a._A__hidden)

class B(A):
    def reveal(self):
        return self._A__hidden

b = B()
print(b.reveal())

class C(A):
    def __init__(self):
        super().__init__()
        self.__hidden = 'child secret'

c = C()
print(c._C__hidden)
print(c._A__hidden)"""
"""
class Parent:
    @final
    def show(self):
        print('родительский')

    def __init_subclass__(cls, **kwargs):
        if 'show' in cls.__dict__:
            raise TypeError("нельзя переопределить show")
        super().__init_subclass__(**kwargs)


class Child(Parent):
    def show(self):
        super().show()
        print('дочерний')

print(Child.mro())

c = Child()
c.show()
"""
"""
print(type(object))
print(type(type))

MyClass = type("MyClass", (object,), {'attr': 42})

obj = MyClass()
print(obj.attr)


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"создаем {name}")
        dct['new_attr'] = 100
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    new_attr = None

print(MyClass.new_attr)

class Base:
    def __init_subclass__(cls, **kwargs):
        if "forbidden" in cls.__name__.lower():
            raise TypeError("нельзя наследовать")
        super().__init_subclass__(**kwargs)

class ForbiddenClass(Base):
    pass


class AutoMethodsMeta(type):
    def __new__(cls, name, bases, dct):
        dct['greet'] = lambda self: print(f"hello from {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AutoMethodsMeta):
    def greet(self):
        pass

obj = MyClass()
obj.greet()"""


"""class Point:
    def __init__(self, x=None, y=None):
        self._x = x
        self._y = y

    def point_print(self):
        print(f'Point x={self._x}, y={self._y}')

    def __str__(self):
        return f'Point x={self._x}, y={self._y}'

a = Point(1, 2)
a.point_print()
str_result = str(a)
print(str_result)
print(str(a))

class Number:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("NaN")
        self.value = value"""
# ----------------------------------------------------------------

"""from time import *

current_time = time()
print(current_time)

local_time = localtime()
print(local_time)

utc_time = gmtime()
print(utc_time)

time_tuple = (2023, 10, 10, 14, 30, 0, 0, 0, 0)
seconds = mktime(time_tuple)
print(seconds)

formatted_time = strftime("%Y-%m-%d %H:%M:%S", tuple(localtime()))
print(formatted_time)

time_string = "2025-03-01 12:37:17"
time_struct = strptime(time_string ,"%Y-%m-%d %H:%M:%S")
print(time_struct)"""

#sleep(1)
# ----------------------------------------------------------------
#kiss
"""def add(a, b):
    return a + b

result = add(5, 6)

result = 5 + 6

x = 10
y = x >> 1
y = x // 2"""
# ----------------------------------------------------------------
#dry
"""
print("enter")
name = input("имя")
print(f"привет, {name}")

print("enter")
surname = input("имя")
print(f"привет, {surname}")

def greet_user():
    print("enter")
    name = input("имя")
    print(f"привет, {name}")

greet_user()
greet_user()

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} гав"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} мяу"


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplemented


class Dog(Animal):
    def speak(self):
        return f"{self.name} гав"

class Cat(Animal):
    def speak(self):
        return f"{self.name} мяу"
"""
# ----------------------------------------------------------------
#yagni

"""class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        pass

    def subtract(self, a, b):
        pass # не используется

    def multiply(self, a, b):
        pass # не используется


class Calculator2:
    def __init__(self):
        pass

    def add(self, a, b):
        pass

class BaseUser:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return  self.name

class AdminUser(BaseUser):
    def __init__(self, name, permissions):
        super().__init__(name)
        self.permissions = permissions

class RegularUser(BaseUser):
    def __init__(self, name):
        super().__init__(name)


class User:
    def __init__(self, name):
        self.name = name"""

# ----------------------------------------------------------------
#slap
"""
def process_user():
    name = input("введите имя")
    if not name.strip():
        print("ошибка - пустое")
        return
    print(f"привет, {name}")

def get_user_input():
    return input("введите имя")

def validate_name(name):
    return bool(name.strip())

def greet_user(name):
    print(f"привет, {name}")

def process_user():
    name = get_user_input()
    if not validate_name(name):
        print("ошибка - пустое")
        return
    greet_user(name)


class DataProcessor:
    def process_data(self, filename):
        with open(filename, "r") as file:
            data = file.read()

        processed_data = data.upper()

        with open("output.txt", "w") as file:
            file.write(processed_data)


class DataProcessor2:
    def read_file(self, filename):
        with open(filename, "r") as file:
            data = file.read()

    def process_data(self, data):
        processed_data = data.upper()

    def save_file(self, filename, data):
        with open(filename, "w") as file:
            file.write(data)

    def run(self, input_file, output_file):
        data = self.read_file(input_file)
        processed_data = self.process_data(data)
        self.save_file(output_file, processed_data)"""
# ----------------------------------------------------------------
#solid
#s - srp

class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        return sum(self.data) / len (self.data)

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(str(self.data))

class Statistics:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        return sum(self.data) / len (self.data)


class FileManager:
    def save_to_file(selfself, filename, data):
        with open(filename, "w") as file:
            file.write(str(data))

#o - ocp

class Discount:
    def __init__(self, price):
        self.price = price

    def get_discounted_price(self, customer_type):
        if customer_type == "VIP":
            return self.price * 0.8
        elif customer_type == "Regular":
            return self.price * 0.9
        else:
            return self.price


class Discount:
    def __init__(self, price):
        self.price = price

    def get_discounted_price(self):
            return self.price

class VIPDiscount(Discount):
    def get_discounted_price(self):
        return self.price * 0.8

class RegularDiscount(Discount):
    def get_discounted_price(self):
        return self.price * 0.9

#l - lsp

class Bird:
    def fly(self):
        print("птица летит")

class Penguin(Bird):
    def fly(self):
        return Exception("пингвины не летают")

class Bird:
    pass

class FlyingBird:
    def fly(self):
        print("птица летит")

class Penguin(Bird):
    def swim(self):
        return Exception("пингвин плавает")

#i - isp

class Worker:
    def work(self):
        pass
    def eat(self):
        pass


class Workable:
    def work(self):
        pass

class Eatable:
    def work(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")


class Robot(Workable):
    def work(self):
        print("Робот работает")


#d - dip

class MySQLDatabse:
    def connect(self):
        print("подключение..")

class Application:
    def __init__(self):
        self.database = MySQLDatabse()

    def run(self):
        self.database.connect()

class Database:
    def connect(self):
        pass

class MySQLDatabse(Database):
    def connect(self):
        print("подключение к MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("подключение к PostgreSQL")


class Application:
    def __init__(self, database: Database):
        self.database = database

    def run(self):
        self.database.connect()

db = PostgreSQLDatabase()
app = Application(db)
app.run()