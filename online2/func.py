"""def add(a: int, b: int) -> int:
    return a + b

def print_sum(a, b):
    print(a + b)

def some_func2():
    print("some")

def many_returns():
    return 1, 2, 3, 4, 5

print(add(1, 2))
print_sum(1, 2)

a, b, c, d, e = many_returns()
print(a, b, c, d, e)



def some_func():
    pass


a = input()
print(a)

def add(a=0, b=0):
    print(a + b)

add(b=5)"""

"""
рекурсия - функция вызывает саму себя
базовый случай - условие прекращения вызовов
"""
# прямая - f вызывает саму себя
# косвенная - f вызывает другую функцию, которая затем вызывает первую
# линейная - f вызывает себя один раз при вычислении результата
# каскадная - f вызывает себя несколько раз

# каскадная - f вызывает себя несколько раз
"""def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)"""


# n!
# прямая - f вызывает саму себя
# линейная - f вызывает себя один раз при вычислении результата
#abs - модуль числа
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)"""
#              5 * f(5 - 1) = 4 * f(4 - 1) = 3
#               5 *         4       *       3
#5*4*3*2 factorial(2 - 1) =1
#5*4*3*2*1
"""n = 5
result = factorial(n)
print(result)
"""
# линейная - f вызывает себя один раз при вычислении результата

"""def collatz(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return collatz(n // 2)
    return collatz(n * 3 + 1)

def nod(a, b):
    if b == 0:
        return a
    if a < b:
        return nod(b, a)
    return nod(b, a % b)
"""
"""
принимает целое число n и выводит все целые от n до 1 включительно
"""
#базовый случай - если n = 1, то функция просто выводит 1 и завершает работу(рекурсию)
#рекурсивный случай - если n > 1,

"""def print_numbers(n):
    if n == 1:
        print(n)
    else:
        print(n)
        print_numbers(n - 1)

n = 5
print_numbers(n)"""
"""
есть набор чисел
[1, 2, 3]
вывести все возможные комбинации чисел
[2, 1, 3]
[3, 2, 1]

написать рек. f, генерирует и выводит комбинации

Простые задачи:
Выбор каждого числа из набора 
и рекурсивная генерация комбинаций оставшихся чисел 
"""
"""def generate_combinations(nums, current_combination=[]):
    # базовый случай: если набор чисел пустой, выводим текущую комбинацию
    if not nums:
        print(current_combination)
    else:
    # рекурсивный:
        for i in range(len(nums)):
            # создаем новый набор без текущего числа
            new_nums = nums[:i] + nums[i + 1:]
            # добавлять текущее число в комбинацию и рекурсивно генерируем комбинацию
            generate_combinations(new_nums, current_combination + [nums[i]])"""

"""for i, num in enumerate(nums):
            # создаем новый набор без текущего числа
            new_nums = nums[:i] + nums[i + 1:]
            # добавлять текущее число в комбинацию и рекурсивно генерируем комбинацию
            generate_combinations(new_nums, current_combination + [num])"""

"""numbers = [1, 2, 3]
generate_combinations(numbers)"""
"""count = 0
cache = {}
def fibonacci(n):
    global count
    if n in cache:
        return cache[n]

    if n <= 1:
        count += 1
        result = n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = result
    return result

n = 15
result = fibonacci(n)
print(result)
print(count)
for key, value in cache.items():
    print(key, value)
"""

"""
def add(a, b):
    return a + b

def curried_add(a):
    def add_b(b):
        return a + b
    return add_b

add_2 = curried_add(2)
print(add_2(3))

curried_add = lambda a : lambda b : a + b
print(curried_add(2)(3))
"""
#map filter reduce (import functools)

"""from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
print(double(5))
print(multiply(2, 5))"""

"""
*args
**kwargs
"""
#*args
#sum()

"""def sum_numbers(a, b, c):
    return a + b + c"""

"""def sum_numbers(*args):
    return sum(args)"""

"""def sum_numbers(*args):
    result = 0
    for e in args:
        result += e
        print(e)
    return result

print(sum_numbers(1, 2, 3, 5))"""

#**kwargs

"""def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name='alice', age=43, city='moscow')

def show_info(*args, **kwargs):
    print("позиционные", args)
    print("именованные", kwargs)

show_info(1, 2, 3, name='alice', age=43)"""


"""
последовательность передачи:

обычные аргументы
*args
обычные именованные аргументы
**kwargs
"""

"""def demo(a, b, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)"""

"""
распаковка аргументов
*iterable позиционных
**dict именованных
"""
#пример каррирование map filter

def sum_numbers(a, b, c):
    return a + b + c

#*iterable
numbers = [1, 2, 3]

sum_numbers(*numbers) # 1, 2, 3 - как отдельные аргументы
#sum_numbers(1, 2, 3)

values = (10, 20, 30)
print(sum_numbers(*values))

nums = {4, 5, 6}
print(sum_numbers(*nums))
#print(sum_numbers(4, 5, 6))
#print(sum_numbers(6, 4, 5))

first, *rest = [1, 2, 3, 4, 5]
print(first)
print(rest)

*head, last = [1, 2, 3, 4, 5]
print(head)
print(last)

#**dict

def person_info(name, age, city):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

data = {"name": "alice", "age": 25, "city": 'moscow'}
person_info(**data)
#person_info(name= alice age= 25 city =moscow)

data = {"name": "alice"}
person_info(**data, age=30, city='dwv')

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

data = {"name": "alice", "age": 25, "city": 'moscow'}
show_info(**data)

def get_numbers():
    return [1, 2, 3]

a, b, c = get_numbers()
numbers = [10, 20, 30]
print(*numbers, sep='\n')

#ошибки
""" 
def greet(name, age):
    print(name, age)
  
data = {"name": "alice"}
greet(**data)

data = {"name": "alice", "age": 25, "city": 'moscow'}
greet(data)"""