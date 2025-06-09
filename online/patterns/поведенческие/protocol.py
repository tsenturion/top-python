"""
protocol
typing Protocol из typing_extensions(старый)/typing(новый)
mypy
"""

"""
преимущества:
полиформизм без наследования
статическая проверка типов (mypy)
гибкость и масштабируемость
разделение поведения и структуры
"""

"""
Возможности:
методы
свойства
операторные методы (магические)
@property
"""

"""
при исполозновании:
не требует явного наследования
можем наследовать явно для intellisense
"""

"""
связь с другими паттернами
strategy - определим протокол поведения
command - каждая команда просто реализует протокол execute
observer - подписчик реализует протокол update(event: Event)
"""
from typing import Protocol, Iterable

class FileLike(Protocol):
    def read(self) -> str:
        ...


def process_file(file: FileLike):
    data = file.read()
    print(data.upper())


class Command(Protocol):
    def execute(self) -> None:
        ...

class PrintCommand:
    def __init__(self, text: str):
        self.text = text

    def execute(self) -> None:
        print(self.text)

class SaveCommand:
    def __init__(self, text: str):
        self.text = text
        
    def execute(self) -> None:
        with open("output.txt", 'w') as f:
            f.write(self.text)

def run_command(cmd: Command):
    cmd.execute()

class HasName(Protocol):
    @property
    def name(self) -> str:
        ...

#from typing import Protocol, Iterable
class SequenceLike(Protocol):
    def __getitem__(self, index: int) -> str:
        ...
    def __len__(self) -> int:
        ...

def print_elements(s: SequenceLike):
    for i in range(len(s)):
        print(s[i])

"""
protocol
протокол Drawable
классы Circle, Square, Image - для каждого draw()
без наследования
"""

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def draw(self) -> None:
        print(f"рисуем с радиус {self.radius}")

class Square:
    def __init__(self, side: int):
        self.side = side

    def draw(self) -> None:
        print(f"квадрат с сторона {self.side}")

class TextBlock:
    def __init__(self, text: str):
        self.text = text

    def draw(self) -> None:
        print(f"текст {self.text}")

def render_scene(drawables: list[Drawable]) -> None:
    print('начало')
    for drawable in drawables:
        drawable.draw()
    print('конец')


circle1 = Circle(10)
square1 = Square(5)
text1 = TextBlock("hi")

scene_objects = [circle1, square1, text1]

render_scene(scene_objects)

"""
модуль проверки данных
json файлы
csv файлы
api ответы

определить интерфейс валидатора 

DataValidator
    validate

EmailValidator - валидация - проверка наличия и формат "email"
AgeValidator - валидация "age" - наличие, положительное число, меньше 0 - 120
UsernameValidator - валидация "username" - наличие, длинна больше 3 символов до 20, 
наличие только буквенно-цифровых символов

run_validators(data: dict, validators: List[DataValidator]) -> List[str]
"""
#from typing import Protocol
from typing import List
import re

class DataValidator(Protocol):
    def validate(self, data: dict) -> bool:
        ...

class EmailValidator:
    def validate(self, data: dict) -> bool:
        email = data.get('email', '')
        return isinstance(email, str) and re.match(r'\S+@\S+\.\S+', email)

class AgeValidator:
    def validate(self, data: dict) -> bool:
        age = data.get('age')
        return isinstance(age, int) and 0 <= age <= 120

class UsernameValidator:
    def validate(self, data: dict) -> bool:
        username = data.get('username', '')
        return isinstance(username, str) and username.isalnum() and 3 <= len(username) <= 20

def run_validators(data: dict, validators: List[DataValidator]) -> List[str]:
    errors = []
    for validator in validators:
        if not validator.validate(data):
            errors.append(f"Ошибка валидации: {validator.__class__.__name__}")
    return errors

validators = [EmailValidator(), AgeValidator(), UsernameValidator()]

data1 = {'email': 'user@example.com', 'age': 30, 'username': 'user123'}
data2 = {'email': 'invalid_email', 'age': 150, 'username': 'user!'}
data3 = {'email': 'invalid_email', 'age': 25, 'username': 'validusername'}
data4 = {'email': '', 'age': None, 'username': ''}

for i, data in enumerate([data1, data2, data3, data4], start=1):
    print(f"Данные {i}:")
    result = run_validators(data, validators)
    if not result:
        print("Данные валидны.")
    else:
        print("Ошибки валидации:")
        for error in result:
            print(error)
    print()
    