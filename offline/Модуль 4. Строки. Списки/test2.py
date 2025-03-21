strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
"""сделать первые буквы заглавными map, lambda"""
repl = lambda x: x.title()
for i in map(repl, strlist):
    print(i)
list2 = list(map(repl, strlist))
print(list2)
list2 = list(map(lambda x: x.title(), strlist))
print(list2)

from functools import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reduce(lambda x, y : x + y, lst))
print(reduce(lambda x, y : x * y, lst))
print(max(lst))
print(reduce(lambda x, y : x if x > y else y, lst))
lststr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#print(' '.join(lststr))
print(reduce(lambda x, y : x + ' ' + y, lststr))
print(reduce(lambda x, y : x + y ** 2, lst))
#print(1 + 2 * 2 + 3 * 3 + 4 * 4 + 5 * 5 + 6 * 6 + 7 * 7 + 8 * 8 + 9 * 9)
n = 9
print(reduce(lambda x, y : x * y, range(1, n + 1)))
#print(reduce(lambda x, y : x * y, lst))
#print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)
#print(min(lst))
print(reduce(lambda x, y : x if x < y else y, lst))
print(reduce(lambda acc, x : acc + 1 if x % 2 == 0 else acc, lst, 0))