"""
r - чтение
w - запись
a - добавление 
x - создание
b - бинарный режим (rb, wb)
+ - сочетание (r+, w+)
"""

file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

"""
open()
.read() - все содержимое файла в одну строку
.readlines() - список строк
.readline() - одну строка
.close()
.writelines() - запись строк. \n не добавляется
.write() - запись
"""

file = open('example.txt', 'w')
file.write('привет мир\n')
file.write('новая строка\n')
file.close()

file = open('example.txt', 'a')
file.write('доп строка\n')
file.close()

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'w') as file:
    file.write('новая запись\n')


try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("файл не найден")
except PermissionError:
    print('нет доступа')


with open('source.txt', 'r') as src:
    content = src.read()

with open('destination.txt', 'w', encoding='utf-8') as dst:
    dst.write(content)


with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

lines = ['1\n', '2\n', '3\n']
with open('myfile.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
