# :=

# variable := expression

print(num := 7)
print(num)

list1 = list(range(11))

# 1
if (length := len (list1)) > 10:
    print(f"список слишком большой ({length} эл.)")

# 2
numbers = [1, 2, 3, 4, 5]
squares = [(square := x ** 2) for x in numbers]
print(squares)
print(square)

#3
data = [5, 4, 3, 2]
c = 0; print([(c := c + x) for x in data])
print(c)

#4
import re
text = "моя почта 1@1.ru"
if match := re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}\b', text):
    print(f"почта найдена {match.group()}")

#5 any all

numbers = [1, 2, 3, 4, 5, 11, 12]
if any((value := number) > 10 for number in numbers):
    print(f"первое > 10: {value}")

# 6
from datetime import datetime

print(f"сегодня {(today := datetime.today()):%Y-%m-%d}, {today:%A}")

