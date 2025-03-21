"""
int - числа
str - строки
float - 1.1  плавающей (точкой)
bool - True False
list - список
"""
"""
number = 10
str1 = '112'
str_number = "34"""

"""num1 = input()
print(num1 + 1)"""

'''dceeve''' #многострочный
#92hrf9ejf39 - однострочный
"""
функции
int()
str()
float()
bool()
list()
"""

"""num1 = int(input())
print(num1 + 1)
"""

"""try:
    num1 = input()
    print(1 / 0)
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("тест прошел")
finally:
    print("тест закончился")"""
""""""

#print(f'{number + 10}, что угодно {str1}')
"""print(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
average_grade = 1.111111111
print(f"{average_grade:.2f}")"""
"""average_grade = 1.111111111

#a = input()

flag1 = True
flag2 = False"""

"""
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

"""boolean_value = 6 > 2 and False or flag1
print(boolean_value)"""
"""number = int(input())
if number > 5:
    print(f"{number} > 5")
elif number < 5:
    print(f"{number} < 5")
else:
    print(f"{number} = 5")"""
"""count = 0
while count < 10 and True:
    if count == 5:
        count += 1
        continue
    if count == 8:
        break
    print(count)
    count += 1
else:
    print("цикл завершился")
"""

"""str2 = """
"""\n
ed
           \t
           w  wv fvff
ewewew"""
"""

str1 = '1234'
for el in str1:
    print(type(el).__name__)
"""

"""print(list(range(5, 50, 10)))
print(list(range(50, 5, -10)))
print(list(range(5, 50, -10)))

list1 = []
list2 = [1, 23, 4,  66, 7,7,8 ,8, True, "23ed", [234, True]]
print(24 in list2)
for e in list2:
    print(e)

print(list(range(0, 5, 2)))
for _ in range(0, 5, 2):
    print("всем привет")"""

#range (начало, конец (не включая), шаг)
"""
range(0, 5, 2)
начало             0
конец (не включая) 5
шаг                2
0 + 2 = 2
2 + 2 = 4
4 + 2 = 6 - вышли за пределы

result = [0, 2, 4]
"""
"""print("-------")
sum = 0
for index in range(3):
    sum += index
    print(index)
print("-------")
print(sum)
"""

"""
some_number = 2.229
print(f'erfger {some_number:.2f} ') #округление до двух знаков

chr() символ по юникод коду
hex() 16x

len() длина 
abs() модуль
max()
min()
sum()

in print('6' in 'absolute')
as 
"""
"""try:
    num1 = input()
    print(1 / 0)
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("тест не прошел")
finally:
    print("тест закончился")

import math as m
from math import pow as p
from math import *

import math

print(m.pi)
print(p(2, 2))
import func
from func import local_func
print(local_func)
"""
"""
операции
//
"""

"""if None:
    print(True)
else:
    print(False)

print(1)
num = print(1)
print(num)
a = max(1, 2)"""

"""
+
-
/
*

% - остаток от деления
// - целочисленное деление
** - возведение в степень
"""

"""print(7 // 2)
print(4001 % 2 == 0)

# Считать с консоли номер дня недели. Вывести буквенную интерпретацию
day = int(input("введите день недели"))"""
"""if day == 1:
    print('monday')
elif day == 2:
    print('втроник')
elif day == 2:  print('втроник')
elif day==  2:  print('втроник')
elif day == 2:
    print('втроник')
elif day == 2:
    print('втроник')
elif day == 2:
    print('втроник')
    """
"""match day:
    case 1: print("пн")
    case 2: print("")
    case 3: print("")
    case 4: print("")
    case 5: print("")
    case 6: print("")
    case 7: print("")
    case _: print("нет")

print(round(1.1))

text = "Hello"
encoded = [ord(c) for c in text]

for c in text:
    print(c, ord(c))

print(encoded)
print("".join(chr(a) for a in encoded))"""

"""# работа с типами данных
my_variable: str = "123"

def greet(name: str) -> str:
    return f"hi, {name}"

print(greet("name"))

# import mypy

def sum_numbers(a: int, b: int) -> int:
    return a + b

print(sum_numbers(1, 1))
print(sum_numbers("1", "1"))
#print(sum_numbers("1", 1))

#isinstance()
class A:
    pass

def process_data(data):
    if isinstance(data, (A, int)):
        print(A, '/', int)
    elif isinstance(data, dict):
        print(dict)
    else:
        print("неверный тип данных")

process_data(5)
"""
"""
console.log(Math.round(num)); //до ближайшего целого
console.log(Math.floor(num)); //округление вниз до ближайшего целого
console.log(Math.ceil(num)); //вверх до ближайшего целого
console.log(Math.trunc(num)); //убрать дробную часть
console.log(num.toFixed(2)); //определенное количество знаков после запятой
"""
num1 = 1.5555
print(round(num1, 2))  # Обычное округление
print(int(num1))  # обрезает
from  math import ceil, floor, trunc
print(ceil(num1))
print(floor(num1))
print(trunc(num1))

