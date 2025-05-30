"""
адаптер позволяет объектам с несовместимыми
интерфейсами работать вместе

+
старую систему с новыми объектами
интегрируем внешнюю библиотеку
унифицировать интерфейсы
перевести объект в понятный формат

подходы
адаптер на уровне объектов - композиция
адаптер на уровне классов - через множественное наследование

структура
target - целевой интерфейс
adaptee - адаптируемый объект
adapter

facade
decorator
bridge
"""

class OldPrinter:
    def print_text(self, text: str):
        print(f'[OLD] {text}')

class NewPrinter:
    def send(self, data: str):
        print(f"[NEW] {data}")

class PrintAdapter:
    def __init__(self, adaptee: NewPrinter):
        self.adaptee = adaptee

    def print_text(self, text: str):
        self.adaptee.send(text)

def client_code(printer):
    printer.print_text("hi")

old = OldPrinter()
client_code(old)

new = NewPrinter()
adapter = PrintAdapter(new)
client_code(adapter)