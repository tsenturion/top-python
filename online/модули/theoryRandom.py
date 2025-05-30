import math, random, re, string
from random import *
print(random()) # случайное от 0 до 1
print(randint(1, 10)) # случайное целое от а до б
list1 = [i * 8 for i in range(5)]
print(choice(list1)) # случайное из последовательности
print(choices(list1, k=2)) # несколько случайных из последовательности
shuffle(list1) # перемешать элементы
print(list1)
print(uniform(1.5, 5.6)) # случайное дробное от а до б
print(randrange(0, 100, 5))
print(sample(list1, k=2))