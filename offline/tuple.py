tuple1 = tuple([1, 2, 3, 4]) # приводит к неизменияемому типу данных
print(tuple1)
tup = (1, 2, 4, '123')
zero_tuple = tuple()
zero_tuple = ()
print(tup)
print(type(tup).__name__)
tup2 = ([], 1, 2, 4, '123')
print(tup)
tup2[0].append(1)
print(tup * 2)

print(tup[1:3])

print(tup + tup2)
print(2 in tup)
print(len(tup))
for i in tup:
    print(i)
from dict import value
"""to_search = input()
data = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
amount = 0
for e in data:
    if e == to_search or e.find(to_search) > 0:
        amount += 1
print(amount)"""
"""data = ("qwe", "qwer", "qwert", "qwerty", "qwer", "qwert", "qwerty", "qwerty")
title = input()
to_replace = input()
result = tuple(map(lambda x : to_replace if x == title else x, data))
print(result)"""

data = (112, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
length = list(map(lambda x : len(str(x)), data))
result = list(map(lambda x : len([i for i in length if i == x]), length))
to_print = set(map(lambda x, y: f'{x} циф. - {y} эл.', length, result))
for e in to_print:
    print(e)

from collections import Counter
data = (112, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
length_counts = Counter(list(map(lambda x : len(str(x)), data)))
to_print = [f'{key} циф. - {value} эл.' for key, value in length_counts.items()]
for e in to_print:
    print(e)

from collections import Counter
data = (112, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
length_counts = Counter(len(str(x)) for x in data)
for key, value in length_counts.items():
    print(f'{key} циф. - {value} эл.')

data1 = (1312, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
data2 = (1122, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
data3 = (1212, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
set1 = set(data1)
set2 = set(data2)
set3 = set(data3)
result = set1.intersection(set2, set3)
result = tuple(result)

data1 = (1312, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
data2 = (1122, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
data3 = (1212, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
set1 = set(data1)
set2 = set(data2)
set3 = set(data3)
unique1 = set1 - set2 - set3
unique2 = set2 - set1 - set3
unique3 = set3 - set1 - set2
result2 = unique1 | unique2 | unique3
result2 = tuple(result2)

# enumerate возвращает пару с индексом и элементом

data1 = (1312, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
data2 = (1122, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
data3 = (1212, 12132, 3133, 1231233, 1234, 1236, 7123123, 123123129)
result3 = tuple(
    x for i, x in enumerate(data1)
    if x == data2[i] == data3[i]
)
for i, x in enumerate(data1):
    print(i, x)
