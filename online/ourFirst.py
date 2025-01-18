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
'''print('frffr', 'ererferfer', 'erfr')
print()
print()
print('frffr', 'ererferfer', 'erfr', sep='0123')
print('frffr', 'ererferfer', 'erfr', sep='\t')
print('frffr', 'ererferfer', 'erfr', sep=' ')
print('frffr', 'ererferfer', 'erfr', sep='??')
print('frffr', 'ererferfer', 'erfr', end='\n')
print('frffr', 'ererferfer', 'erfr', end='\t')
print('frffr', 'ererferfer', 'erfr', end=' ')
print('frffr', 'ererferfer', 'erfr', end='??')'''
keyboard_input = input(int('Введите число от 1 до 100: ')
try:
    number = int(keyboard_input)

if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else: print(number)