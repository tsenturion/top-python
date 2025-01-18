"""from time import *
print(pow(2, 3))
from math import pow
"""
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

""" Решение 1
def is_palindrome(text):
    processed_text = "".join(text.lower().split())
    return processed_text == processed_text[::-1]

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
"""
"""Решение 2
def modify_text(text, reserved_words):

    modified_text = text
    for word in reserved_words:
        modified_text = modified_text.replace(word, word.upper())
    return modified_text

text = input("Введите текст: ")

reserved_words_input = input("Введите зарезервированные слова через запятую: ")
reserved_words = [word.strip() for word in reserved_words_input.split(',')]

modified_text = modify_text(text, reserved_words)
print("Измененный текст:")
print(modified_text)
"""
"""Решение 3
import re

def count_sentences(text):

  sentence_endings = re.compile(r'[.!?]+')
  sentences = sentence_endings.findall(text)
  return len(sentences)

text = input("Введите текст: ")

sentence_count = count_sentences(text)
print("Количество предложений в тексте:", sentence_count)
"""

"""Решение 4
def fizz_buzz(number):

    if not 1 <= number <= 100:
       return "Ошибка: число должно быть в диапазоне от 1 до 100."
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

while True:
    try:
      user_input = int(input("Введите число от 1 до 100: "))
      break
    except ValueError:
       print("Ошибка: пожалуйста, введите целое число.")

result = fizz_buzz(user_input)
print(result)
"""
"""Решение 5
def power_calculator(number):

    print("Выберите степень (от 0 до 7):")
    while True:
      try:
        power = int(input())
        if 0 <= power <= 7:
             break
        else:
             print("Ошибка: введите число от 0 до 7.")
      except ValueError:
         print("Ошибка: введите целое число.")
    result = number ** power
    print(f"{number} в степени {power} = {result}")

while True:
    try:
        user_number = float(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка: введите число.")

power_calculator(user_number)
"""

"""Решение 6

def calculate_call_cost(duration, from_operator, to_operator):

    tariffs = {
        ("A", "A"): 0.5,
        ("A", "B"): 1.0,
        ("A", "C"): 1.2,
        ("B", "A"): 1.0,
        ("B", "B"): 0.6,
        ("B", "C"): 1.1,
        ("C", "A"): 1.2,
        ("C", "B"): 1.1,
        ("C", "C"): 0.7,
    }

    if (from_operator, to_operator) not in tariffs:
        return "Ошибка: Неизвестная комбинация операторов."

    cost_per_minute = tariffs[(from_operator, to_operator)]
    cost = duration * cost_per_minute
    return cost

while True:
  try:
     duration = float(input("Введите длительность разговора (в минутах): "))
     if duration >= 0:
        break
     else:
        print("Ошибка: длительность разговора не может быть отрицательной.")
  except ValueError:
      print("Ошибка: пожалуйста, введите число.")

while True:
   from_operator = input("Выберите оператора, с которого звонят (A, B, C): ").upper()
   if from_operator in ["A", "B", "C"]:
        break
   else:
        print("Ошибка: выберите оператора из списка A, B, C.")

while True:
    to_operator = input("Выберите оператора, на который звонят (A, B, C): ").upper()
    if to_operator in ["A", "B", "C"]:
         break
    else:
         print("Ошибка: выберите оператора из списка A, B, C.")


cost = calculate_call_cost(duration, from_operator, to_operator)

if isinstance(cost, str):
    print(cost)
else:
    print(f"Стоимость разговора: {cost:.2f} руб.")
"""

"""Решение 7

def calculate_salary(sales):

    base_salary = 200
    if sales <= 500:
        bonus_percentage = 0.03
    elif sales <= 1000:
        bonus_percentage = 0.05
    else:
        bonus_percentage = 0.08
    bonus = sales * bonus_percentage
    salary = base_salary + bonus
    return salary

def find_best_manager(sales_list):

    best_manager_index = 0
    best_sales = sales_list[0]
    for i, sales in enumerate(sales_list):
        if sales > best_sales:
           best_sales = sales
           best_manager_index = i
    return best_manager_index

sales_list = []
for i in range(3):
   while True:
      try:
         sales = float(input(f"Введите объем продаж для менеджера {i+1}: "))
         if sales >= 0:
            sales_list.append(sales)
            break
         else:
            print("Ошибка: уровень продаж не может быть отрицательным.")
      except ValueError:
           print("Ошибка: пожалуйста, введите число.")

salaries = [calculate_salary(sales) for sales in sales_list]

best_manager_index = find_best_manager(sales_list)

salaries[best_manager_index] += 200

print("\nИтоги:")
for i, salary in enumerate(salaries):
    print(f"Зарплата менеджера {i+1}: {salary:.2f}$")

print(f"\nЛучший менеджер: {best_manager_index+1}")
print(f"Зарплата лучшего менеджера с премией: {salaries[best_manager_index]:.2f}$")
"""

"""Решение 8

def is_prime(number):

    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_in_range(start, end):

    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
           primes.append(number)
    return primes

while True:
   try:
      start = int(input("Введите начало диапазона: "))
      end = int(input("Введите конец диапазона: "))
      if start >= 0 and end >= start:
         break
      else:
         print("Ошибка: начало диапазона не может быть отрицательным и не должно превышать конец диапазона")
   except ValueError:
       print("Ошибка: пожалуйста, введите целые числа.")

prime_numbers = find_primes_in_range(start, end)
print(f"Простые числа в диапазоне от {start} до {end}: {prime_numbers}")
"""
"""Решение 9

def print_multiplication_table():

  for i in range(1, 11):
    for j in range(1, 11):
      print(f"{i} * {j} = {i * j:<4}", end="  ")
    print()

print_multiplication_table()
"""

"""Решение 10

def print_multiplication_table_range(start, end):

    for i in range(start, end + 1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j:<4}", end="  ")
        print()

while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if start >= 0 and end >= start:
            break
        else:
           print("Ошибка: начало диапазона не может быть отрицательным и не должно превышать конец диапазона")
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа.")

print_multiplication_table_range(start, end)
"""

