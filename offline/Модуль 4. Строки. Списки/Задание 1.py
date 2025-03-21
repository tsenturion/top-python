#arithmetic_expression = input("Введите арифметическое выражение: ")
from re import findall

arithmetic_expression = "23+12"
result = 0

numbers = findall(r'\d+', arithmetic_expression)
number1 = int(numbers[0])
number2 = int(numbers[1])
print(number1)
print(number2)

for i in arithmetic_expression:
    if i == '+':
        result = number1 + number2
    elif i == '-':
        result = number1 - number2
    elif i == '*':
        result = number1 * number2
    elif i == '/':
        result = number1 / number2
print(result)




