"""
1402_map
"""

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)

def square(x):
    return x * x

result = list(map(square, numbers))
print(result)