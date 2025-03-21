from random import randint, randrange

list = []
positive = 0
negative = 0

for i in range(50):
    list.append(randint(-5, 5))
for i in list:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print(f'В списке {list}\n{positive} положительных чисел\n{negative} отрицательных чисел\n{list.count(0)} нулей')