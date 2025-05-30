def sqr1(number):
    return number * number

def printf(some_list, func):
    """docstring"""
    for i in some_list:
        print(func(i))


list1 = list(range(5))

printf(list1, sqr1)
printf(list1, lambda x : x * x)


sqr = lambda x : x * x

print(sqr(5))
for i in map(sqr1, list1):
    print(i)
list2 = list(map(sqr1, list1))
print(list2)

for i in filter(lambda x : x % 2 == 0, list1):
    print(i)
list1 = list(filter(lambda x : x % 2 == 0, list1))
print(list1)
fib = lambda n : n if n <= 1 else fib(n - 1) + fib(n - 2)
fact = lambda n : 1 if n == 0 else n * fact(n - 1)

#vfact = lambda f: f(f, n)
#infact = lambda n :
fact2 = lambda f , x :  1 if x == 0 else x * f(f, x - 1)
ifact = lambda n : (lambda f: f(f, n))(fact2)

list1 = list(map(fib, range(10)))
list2 = list(map(fact, range(10)))
print(list1)
print(list2)

strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
"""сделать первые буквы заглавными map, lambda"""

strlist = list(map(lambda n : n.title(), strlist))

numlist = ['1 2 3 4', '1 2 3 4', '1 2 3 4', '1 2 3 4']
"""найти сумму элементов map, lambda, .split()numlist = [10, 10, 10, 10]"""
numlist = list(map(lambda s: sum(map(int, s.split())), numlist))

strlist = ['121', 'fsd1231', 'fsd1231', 'Rsd1231', 'Rsd1231']
"""список слов с заглавной буквы, сделать их прописными filter
strlist = ['rsd1231', 'rsd1231']"""
strlist = list(map(lambda x : x.lower(), filter(lambda x : x.istitle(), strlist)))

strlist = ['121', '123321', 'fsd1231', 'Rsd1231', 'Rsd1231']
"""одинаково слева направо strlist = ['121', '123321']"""

strlist = list(filter(lambda x : x == x[::-1], strlist))

strlist = ['a', '123321', 'fsd1231', 'ii', 'Rsd1231']
"""с любой гласной aeiouyAEIOUY"""
strlist = ['a', 'ii']
b = "aeiouyAEIOUY"
strlist = list(filter(lambda x: any(ch in b for ch in x), strlist))
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Удвойте каждый элемент списка чисел.
print(list(map(lambda x : x * 2, numbers)))

# Отфильтруйте чётные числа из списка.
print(list(filter(lambda x : x % 2 == 0, numbers)))

# Преобразуйте все строки в списке в верхний регистр.
strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
print(list(map(lambda s : s.upper(), strlist)))

# Отфильтруйте положительные числа из списка.
print(list(filter(lambda x : x > 0, numbers)))

# Вычислите квадраты всех чисел в списке.
print(list(map(lambda x : x ** 2, numbers)))

# Отфильтруйте чётные числа, а затем возведите их в квадрат. map filter
print(list(map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, numbers))))