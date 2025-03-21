"""
list - список
"""
list1 = [1, 2, [3, 4, 5], {5, 6, 7}, (5, 6, 7), "6", True]
list2 = []

# bool - булевый - boolean
flag1 = True
flag2 = False

#str
str1 = "1"
str2 = '1'

print(f"{flag1} and {flag2}")
print(1, 2, 3, 4, end='\n', sep='')
print(1, 2, 3, 4, end='')
print(1, 2, 3, 4, end='')

#int
a = 1
#float
b = 1.1

#tuple
#dict
#set
#frozenset

"""
False:

False
None (nil/null)
[]
''
""
0
0.0
()
{}
"""

if 0.0:
    print(True)
else:
    print(False)

"""
>
<
<=
>=
== - равно
!= - не равно

and
or
not

is
"""

flag3 = False and True or False and True
#        0     *    1   +  0     *    1
flag4 = not True

flag5 = 5 > 3 and 7 < 8 or not 5 > 3

if 5 > 2:
    print(True)
elif 5 < 1:
    print(True)
else:
    print(False)

count = 0
while count < 10:
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1
    if count == 9:
        break

else:
    print("цикл закончился")

for e in list1:
    print(e)

print(range(5))
print(list(range(5)))

for _ in range(5):
    print("привет")

"""
range (начало, конец, шаг)
range (начало, конец)
range (конец)
"""
for i in range(1, 50, 7):
    print(i, end=' ')
else:
    print("цикл завершился")


try:
    num1 = int(input())
    if num1 != 0:
        print(1 / num1)

except ZeroDivisionError as ex:
    print(ex)
    print(ZeroDivisionError)
except TypeError as ex:
    print(ex)
    print(TypeError)
except Exception as ex:
    print(ex)
    print(Exception)
else:
    print("тест прошел")
finally:
    print("тест закончился")

list2 = [1, 2]

match list2:
    case [1, 2]:
        print(True)