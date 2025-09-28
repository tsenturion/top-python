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
import re
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

with open('txts/region.txt', 'r') as file:
    pat = r'ASIA'
    while lines != "":
        lines = file.readlines()
        if re.match(pat, lines):
            reg = lines[0]
            break
    print(lines)
reg = -1
nat = []
amount = 0
with open('txts/region.txt', 'r') as file:
    lines = file.readlines()
    to_find = 'ASIA'
    # content = file.read()
    for line in lines:
        if to_find in map(lambda s : s.strip(), line.split('|')):
            reg = line[0]
            break
    """for line in lines:
        if line.find(to_find) > 0:
            reg2 = line[0]
            break"""
with open('txts/nation.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if reg in line.split('|')[2]:
            nat.append(line.split('|')[0])
with open('txts/customer.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.split('|')[3] in nat:
            amount += 1
print(amount)

