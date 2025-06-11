import sys
# python myscript.py input.txt output.txt
print(sys.argv) # ['myscript.py', 'input.txt', 'output.txt']

"""input_file = sys.argv[1]
output_file = sys.argv[2]"""

"""if len(sys.argv) < 3:
    print("Please provide input and output files.")
    sys.exit(1)"""


"""if not valid_data:
    print('Please provide valid data.')
    sys.exit(1)"""

print(sys.platform)
if sys.platform.startswith('win'):
    print('windows')


print(sys.version)
print(sys.version_info)

if sys.version_info[1] < 12:
    print('Your version is too low.')
else:
    print('Your version is high.')


import math
print('math' in sys.modules)

print(sys.path)
for path in sys.path:
    print(path)
# sys.path.append('/home/kenny090607/')

"""
sys.stdin ввод
sys.stdout вывод
sys.stderr ошибки
input()
print()
"""

"""text = sys.stdin.readline()
sys.stdout.write(text)
sys.stderr.write('Error')"""

a = [1, 2, 3, 4]
print(sys.getsizeof(a))

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

print(sys.flags.optimize)

"""with open('log.txt', 'w') as log_file:
    sys.stdout = log_file
    print('это печатается в файл')"""

"""
file_filder.py

принимает два аргумента командной строки
    путь к папке, в которой будут искаться файлы
    расширение файлов, которые нужно найти (.txt)

проверка
    что переданы два аргумента
    что путь к папке существует и это папка

проходит по всей вложенной структуре папок (os.walk() или без вложенности)
    ищет файлы с нужным расширением
    выводит список файлов на экран
    общее количества таких файлов и размер

обработка ошибок
    выводим сообщение об ошибке в sys.stderr и завершаем с 0


os.walk()
"""

import os
import sys

def print_error(message):
    sys.stderr.write(f"Ошибка: {message}\n")
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print_error("Необходимо передать два аргумента: путь к папке и расширение файлов.")

    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.exists(directory):
        print_error(f"Путь '{directory}' не существует.")
    if not os.path.isdir(directory):
        print_error(f"Путь '{directory}' не является директорией.")

    total_files = 0
    total_size = 0
    matched_files = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(extension):
                file_path = os.path.join(root, name)
                try:
                    size = os.path.getsize(file_path)
                except OSError:
                    continue

                total_files += 1
                total_size += size

                relative_path = os.path.relpath(file_path, start=directory)
                matched_files.append((relative_path, size))

    print(f'Найдено {total_files} файлов с расширением "{extension}":')

    for path, size in matched_files:
        print(f"- {os.path.join(directory, path)} ({size} байт)")

    print(f"\nОбщий размер: {total_size} байт")

if __name__ == "__main__":
    main()
