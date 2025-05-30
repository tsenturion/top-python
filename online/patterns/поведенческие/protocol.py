"""
protocol
typing Protocol из typing_extensions(старый)/typing(новый)
mypy
"""

"""
полиформизм без наследования
статическая проверка типов (mypy)
"""

"""
методы
свойства
операторные методы (магические)
"""

"""
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
        with open("output.txt", 'w') as f:
            f.write(self.text)

def run_command(cmd: Command):
    cmd.execute()

class HasName(Protocol):
    @property
    def name(self) -> str:
        ...

class SequenceLike(Protocol):
    def __getitem__(self, index: int) -> str:
        ...
    def __len__(self) -> int:
        ...

def print_elements(s: SequenceLike):
    for i in range(len(s)):
        print(s[i])

