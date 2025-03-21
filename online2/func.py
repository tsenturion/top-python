def add(a, b):
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