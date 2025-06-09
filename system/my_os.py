import os

print(os.getcwd())  # C:\Users\Ефимов\pythonProjects\top-python
print(os.environ['TEMP']) # C:\Users\Ефимов\AppData\Local\Temp
print(os.environ['USERPROFILE']) # C:\Users\Ефимов
os.environ['MY_VAR'] = 'SOME_VALUE'
print(os.environ['MY_VAR']) # SOME_VALUE
os.chdir('C:/Users/Ефимов/pythonProjects/') #перемещение в 
print(os.getcwd())
try:
    os.mkdir('new_dir_1') # создание папки
    os.makedirs('new_dir/new_dir_1/new_dir_2') # создание папки с вложенными папками
except FileExistsError:
    print('Такая папка уже существует')
    
os.rmdir('new_dir_1') # удаление папки
os.removedirs('new_dir/new_dir_1/new_dir_2') # удаление папки с вложенными папками (папка должна быть пустой)


print(os.path.exists('new_dir')) # проверка существования файла или папки

# os.remove('pythonProject.rar') # удаление файла

files = os.listdir() # список файлов в текущей директории
print(files)

for file in os.listdir():
    if file.endswith('.txt'):
        print(file)

path = os.path.join('folder', 'file.txt') # создание пути к файлу кросплатформенно
print(path)


print('-' * 20)
print(os.path.basename('/path/to/file.txt')) # название файла
print(os.path.dirname('/path/to/file.txt')) # название директории
print(os.path.split('/path/to/file.txt')) # кортеж из двух элементов
print('-' * 20)
print(os.path.isfile('folder/file.txt')) # проверка является ли путь файлом
print(os.path.isfile('temp.txt')) # проверка является ли путь файлом
print(os.path.isdir('folder')) # проверка является ли путь директорией
print('-' * 20)
size = os.path.getsize('temp.txt') # размер файла
print(size)

import time
mod_time = os.path.getmtime('temp.txt') # время модификации файла
print(time.ctime(mod_time)) # преобразуем в читаемую дату

if os.name == 'nt':
    print('Windows')
elif os.name == 'posix':
    print('Mac OS/Linux/Unix')
else:
    print('Other')
    
# print(os.system('dir'))


"""
проходит по папке, ищет файлы с расширением .txt, выводит их размер
(предполагается 4 строчки кода)
"""
folder = '.'

for name in os.listdir(folder):
    path = os.path.join(folder, name)
    if os.path.isfile(path) and name.endswith('.txt'):
        print(f'{path}: {os.path.getsize(path)}')