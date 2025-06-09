from pathlib import Path
p = Path('some_folder') # относительный путь
p2 = Path('/usr/bin') # абсолютный путь
p = Path('some_folder/file.txt')
abs_path = p.resolve() # абсолютный путь
print(abs_path)
print('-' * 20)
# os.path.join(p1, p2) /
base = Path('/home/user')
file = base / 'documents' / 'notes.txt'

p = Path('/home/user/docs/report.txt')

print(p.name) # название файла = report.txt
print(p.stem) # название файла без расширения = report
print(p.suffix) # расширение файла = .txt
print(p.parent) # путь к папке = /home/user/docs
print(p.parts) # кортеж всех частей пути = ('/', 'home', 'user', 'docs', 'report.txt')

print(p.exists()) # проверка существования пути = True/False
print(p.is_file()) # проверка на файл = True/False
print(p.is_dir()) # проверка на директорию = True/False

"""p = Path('example.txt')

p.write_text('Пример текста') # запись текста в файл

text = p.read_text() # чтение текста из файла

data = p.read_bytes() # чтение бинарных данных из файла
p.write_bytes(data) # запись бинарных данных в файл
b'1231'
str.encode() # преобразование строки в байты
print(text)
"""


"""p = Path('some_folder')
p.mkdir() # создание директории
p.mkdir(parents=True, exists_ok=True) # создание директории и ее родительских директорий"""

# p.unlink() # удаление файла
# p.rmdir() # удаление пустой директории

for item in Path('.').iterdir():
    print(item)

# примеры шаблонов *.py, data_??.csv */logs/*.log
for txt_file in Path('.').glob('*.txt'):
    print(txt_file)

for py_file in Path('.').rglob('*.py'):
    print(py_file)


# поиск всех .log файлов в каталоге logs и вывод их размеров
logs_dir = Path('logs')
for log_file in logs_dir.rglob('*.log'):
    size = log_file.stat().st_size # размер файла в байтах
    print(log_file, size)
else:
    print('не найдено')

# создание структуры проекта
"""base = Path('my_project')
(base / 'data').mkdir(parents=True, exist_ok=True)
(base / 'scripts').mkdir(parents=True, exist_ok=True)
(base / 'README.md').write_text('Описание проекта')"""

# удаление пустых директорий
"""for folder in Path('.').rglob('*'):
    if folder.is_dir() and not any(folder.iterdir()):
        folder.rmdir()
        print('удалена пустая директория', folder)"""

print(logs_dir)
print(str(logs_dir))

"""with open(str(logs_dir), 'w') as file:
    pass"""

from pathlib import PureWindowsPath, PurePosixPath
p = PureWindowsPath('C:/Windows/System32')
print(p)

"""
ищет все файлы в указанной папке (включая вложенные)
выбирает только файлы
    размером больше заданного порога (в байтах)
    и которые были изменены за последние N дней
выводит 
    полный путь к файлу
    размер файла
    время последнего изменения

file.stat().st_mtime - время последнего изменения файла в секундах с начала эпохи Unix (1 января 1970 года)
datetime.fromtimestamp() - для даты изменения
datetime.now() - текущая дата и время
"""

#from pathlib import Path
from datetime import datetime, timedelta

target_dir = Path('.')
min_size = 10_000 # минимальный размер файла в байтах
days = 30 # количество дней

now = datetime.now()
time_limit = now - timedelta(days=days)

for file in target_dir.rglob('*'):
    if file.is_file():
        stat = file.stat()
        file_size = stat.st_size
        file_mtime = datetime.fromtimestamp(stat.st_mtime)

        if file_size >= min_size and file_mtime >= time_limit:
            print(f"- {file.resolve()}\n  размер: {file_size} байт\n  время изменения: {file_mtime}")