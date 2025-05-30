"""

"""
"""
pickle - объекты
json - 
marshal
csv (pandas для работы)
yaml, protobuf, msgpack
"""

"""
.dump
.dumps - байты
.load() - читает содержимое и восстанавливает объект
.loads() - для байт
"""
import pickle
data = {'name': 'John', 'age': 30, 'skills': ['python', 'java', 'c++']}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

nums = [1, 2, 3, 4, 5]
with open('numbers.pkl', 'wb') as file:
    pickle.dump(nums, file)



"""
.dump
.dumps - строку
ensure_ascii= - позволяет сохранять кириллицу
indent= - форматирует json (отступы)
.load() - читает содержимое и восстанавливает объект
.loads() - для строки
"""
import json

data = {'name': 'John', 'age': 30, 'skills': ['python', 'java', 'c++']}

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

"""
{
    "name": "John",
    "age": 30,
    "skills": [
        "python",
        "java",
        "c++"
    ]
}
"""

users = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
]
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)


data = {'key1': 'value1'}
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

data = {"x": 1, "y": 2}
binary_data = pickle.dumps(data)
print(binary_data)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)


with open('person.pkl', 'rb') as file:
    person = pickle.load(file)

print(person)

data = pickle.loads(pickle_bytes) 

with open('data.pkl', 'wb') as file:
    pickle.dump(obj1, f)
    pickle.dump(obj2, f)

with open('data.pkl', 'rb') as file:
    obj1 = pickle.load(file)
    obj2 = pickle.load(file)

#import json
with open('user.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)

json_str = '{"name": "John", "age": 30}'
data = json.loads(json_str)
print(data)

"""
ошибки для обработки
EOFError - конец файла
UnicodeDecodeError - не верная кодировка
json.decoder.JSONDecodeError - не верный формат
AttributeError - не верный объект
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

with open('students.pkl', 'rb') as file:
    obj = pickle.load(file)

print(obj.name, obj.age)

# {"name": "John", "age": 30}

#import pickle
data = client_input
obj = pickle.loads(data)

"""
import os

class Evil:
    # def __reduce__(self):
        # return (os.system, ('rm - rf /'))
        
malicious_data = pickle.dumps(Evil())
"""
"""import platform
import platform as pl
from platform import architecture
from platform import architecture as arch"""

"""from platform import *

print(architecture())  # архитектура
print(machine())  # тип машины
print(node())  # сетевое имя машины
print(platform())  # строка идентифицирующая базовую платформу
print(processor())  # имя процессора
print(system())  # имя ОС
print(release()) # версия ОС
print(version()) # доп информация об ОС
print(python_version()) # версия питона
print(python_build()) # информация о сборке python
print(python_compiler()) # о компиляторе
pickle.loads(malicious_data)
"""
"""
 - не загружаем из неизвестных/ненадежных источников
 - используем виртуальные окружения или контейнеры для изоляции процесса
 - возможность подписи данных 
 - json/marshal/csv (pandas для работы)/yaml, protobuf, msgpack/dill/xml
"""

