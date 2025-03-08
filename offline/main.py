"""number1 = 1
number2 = 1.1
str1 = '123'
flag1 = True
flag2 = False
print(number1, type(number1).__name__, 2 + 2, sep='', end='')
print(number2, type(number2).__name__)
print(str1, type(str1).__name__)
print(flag1, type(flag1).__name__)
print(flag2, type(flag2).__name__)

# 8093454
"""
from functools import reduce

from fontTools.misc.cython import returns

from offline.strs import sorted1
from offline.tuple import result

"""qwd
qwwwww"""
"""

'''
qwd
qwd
dw
'''"""
"""
num = int(input())
num = str(num)
num = float(num)
num = bool(num)
print(type(num))
print(num)"""
"""flag = 5 > 3 and 6 > 2 and not False or False
print(flag)"""
# >
# <
# >=
# >=
# ==
# !=
"""
if False:
    print(True)
    print(True)
else:
    print(False)
    if True:
        print(True)"""
"""if False:
    print()
elif False:
    print()
elif False:
    print()
else:
    print("finally")"""
"""i = 0
while 5 > 3 and 6 > 2 and not False or False:
    i += 1
else:
    print("done")    
    """
"""str1 = 'vfj2'
numbers = '1234567890'
list1 = [0, 4, 6, 74, '2', True]
for elem in list1:
    if type(i) != int:
        print(i, 'это не число')"""
"""i = 0 
while True:
    i += 1
    if i == 10:
        break
        
for i in range(10):
    if i == 5:
        continue
    print(i)"""

"""
try:
    print(1 / 0)
except Exception as ex:
    print(ex)
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print('ошибок не возникло')
finally:
    print("тест завершен")"""

"""name = input()
print('Hello, ' + name + '!')"""
"""print('!' * 10)"""
"""print(1, 2, 3)
print(1, 2, 3)
print(1, 2, 3, sep='', end='')
print(1, 2, 3, sep='', end='')"""
# min
# max
# abs
# len
# pow
# hex
# round
import math
"""sum1 = sum([1, 2, 3, 4, 5, 6, 7])
max1 = max(1, 2, 3, 4)
min1 = min(1, 2, 4, 5)
abs1 = abs(-1)
someStr = '123z121saf253'
length1 = len([1, 2, 3])
length2 = len(someStr)

sorted1 = sorted(someStr)
print(''.join(sorted1))
sorted2 = sorted([1, 2, 3])

print(any([True, False, False])) # или во множестве
print(all([True, True, True]))  # и во множестве

list1 = []
for i in range(10):
    list1.append(i)
print(list1)"""
"""
import time
import time as t
from time import *
list1 = [1, 2, 3]
first = 0
second = 0
for _ in range(10):
    start = time()
    for _ in range(100000):
        list1.extend([5, 5])
    end = time()
    firstTime = start - end
    list2 = [1, 2, 3]
    start = time()
    for _ in range(100000):
        list2 += [5, 5]
    end = time()
    secondTime = start - end
    if secondTime > firstTime:
        second += 1
    else:
        first += 1
print(f"{first}\n{second}")
print(first)
print(second)"""
# на выборке из 100 определить какой из методов работает быстрее с указанием количества раз для каждого
"""list1 = list(range(2, 200, 20))
print(list1)
print(list1[0:6:2])
list1 = list(range(200, -9, -10))
print(list1)
print(list1[::-1])
msg = '123r'
print(msg.count('r', 5, 10))"""
# print(hex(199))
"""
console.log(Math.round(num)); //до ближайшего целого
console.log(Math.floor(num)); //округление вниз до ближайшего целого
console.log(Math.ceil(num)); //вверх до ближайшего целого
console.log(Math.trunc(num)); //убрать дробную часть
console.log(num.toFixed(2)); //определенное количество знаков после запятой"""
"""print(round(1.4))
import math
print(math.floor(1.3))
msg = ' 3 4 '
print(msg.strip())
print(msg.strip())

def customSum(a, b=0):
    return a + b, 10
result, ok = customSum(7)
print(result)
print(ok)"""
list1 = [1, 2]
"""
from functools import *

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x + y, ['1', '2', '3', '4']))

"""
"""собрать все оценки всех студентов в один список
средний балл по всем """
"""

students = [
    {'name': 'matvey', 'age': 23, 'grades': [1, 2, 3, 4]},
    {'name': 'matvey', 'age': 23, 'grades': [1, 2, 3, 4]},
    {'name': 'matvey', 'age': 23, 'grades': [1, 2, 3, 4]},
    {'name': 'matvey', 'age': 23, 'grades': [1, 2, 3, 4]},
    {'name': 'matvey', 'age': 23, 'grades': [1, 2, 3, 4]},
]
# reduce собрать все оценки в один список
# reduce найти средний балл
#all_grades = reduce(lambda acc, student: acc + student['grades'], students, [])
all_grades = [grade for student in students for grade in student['grades']]
              
all_grades = []
for student in students:
    for grade in student['grades']:
        all_grades.append(grade)
        
total_sum = 0
total_len = 0
for student in students:
    total_len += len(student["grades"])
    total_sum += sum(student["grades"])
    
result = reduce(lambda x, y: x + y, all_grades) / len(all_grades)
print(all_grades)
for i, e in enumerate(list(range(4, 10))):
    print(i, e)"""
"""list1 = [1, 2, 3]
list2 = [1, 2, 3]
zipped = zip(list1, list2)
print(list(zipped))
list4, list5 = zip(*zipped)

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
zipped = zip(list1, list2)
print(list(zipped))
print(list(zip(*zipped)))

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 4, 5, 6, 7]
zipped = zip(list1, list2, list3)
print(list(zipped))
print(list(zip(*zipped)))"""
"""
объеденить чтобы по студенту, для каждого
были доступны имя возраст оценки
найти средний балл по всем
с самым высоким
"""
"""students = [('alice', 20), ('alice', 20), ('alice', 20)]
grades  = [[1, 2, 3], [1, 2, 3], [1, 2, 4]]"""
"""
'alice', 20, [1, 2, 3], 2
'alice', 20, [1, 2, 3], 2
'alice', 20, [1, 2, 4], 2.33

'alice', 20, [1, 2, 4], 2.33

2.11
"""
"""from functools import reduce

students = [('alice', 20), ('alice', 20), ('alice', 20)]
grades = [[1, 2, 3], [1, 2, 3], [1, 2, 4]]

combined_data = list(zip(students, grades))
print(combined_data)
student_averages = []

for (name, age), student_grades in combined_data:
    average_grade = sum(student_grades) / len(student_grades)
    student_averages.append((name, age, student_grades, average_grade))
    print(f"'{name}', {age}, {student_grades}, {average_grade:.2f}")

#all_grades = [grade for student_grades in grades for grade in student_grades]
all_grades = reduce(lambda acc, student_grades: acc + student_grades, grades, [])
overall_average = sum(all_grades) / len(all_grades)

best_student = max(student_averages, key=lambda x: x[3])

print(round(overall_average, 2))
print(best_student[0], best_student[1], best_student[2], round(best_student[3], 2))"""
