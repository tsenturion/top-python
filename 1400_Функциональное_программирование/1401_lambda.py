"""
1401_lambda
"""

def square(x):
    return x * x


square = lambda x: x * x

print(square(5))

def operate(func, value):
    return func(value)

result = operate(lambda x: x * x, 5)
print(result)

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
]
print(sorted(students))
print(sorted(students, key=lambda student: student[1]))

def get_score(student):
    return student[1]

add = lambda x, y: x + y
print(add(3, 5))

def add(x, y):
    return x + y

print(add(3, 5))

multiply = lambda x, y: x * y
print(multiply(4, 6))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(5))


# lambda x: (x * 2 + 5) / 3 if x > 10 else x * 2 - 7

def process_number(x):
    if x > 10:
        return (x * 2 + 5) / 3
    else:
        return x * 2 - 7

print(process_number(15))

# sorted(data, key=lambda item: item[1])

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
sorted_users = sorted(users, key=lambda user: user["age"])
sorted_users = sorted(
    users,
    key=lambda user: user["age"],
)
print(sorted_users)