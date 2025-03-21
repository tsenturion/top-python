"""
чтение
read() - читает весь файл целиком
readlines() - читает файл построчно
read(n) - указанное количество символов

запись
write() - строку в файл
writelines(lines)
"""
"""file = open('txts/region.txt', 'r')
#код
file.close()"""

reg = -1
nat = []
amount = 0

with open('txts/region.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('txts/nation.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('txts/customer.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

print(amount)
