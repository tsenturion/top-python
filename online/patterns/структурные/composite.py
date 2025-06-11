"""
структура:
компонент
leaf
composite контейнер
client

+
прозрачность
расширяемость
рекурсивность

применяем когда
древовидная структура
однаковая обработка элементов
код должен одинаково работать с различными компонентами

decorator - добавление функционала
bridge - разделение абстракции и реализации
chain of responsibility обрабатывает по цепочке
"""

class FileSystemComponent:
    def display(self, indent=0):
        raise NotImplementedError

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + f"File {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children  = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def display(self, indent=0):
        print(' ' * indent + f"Folder {self.name}")
        for child in self.children:
            child.display(indent + 2)

root = Folder("root")
root.add(File("1.txt"))
root.add(File("2.txt"))

sub = Folder("src")
sub.add(File('3.txt'))
sub.add(File('4.txt'))

nested = Folder("tests")
nested.add(File("5.txt"))
nested.add(File("6.txt"))

sub.add(nested)
root.add(sub)

root.display()

"""
composite

MenuComponent
MenuItem
MenuGroup
render
"""

class MenuComponent:
    def render(self, indent=0):
        raise NotImplementedError

class MenuItem(MenuComponent):
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def render(self, indent=0):
        print(' ' * indent + f'{self.title} ({self.link})')

class MenuGroup(MenuComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component: MenuComponent):
        self.children.append(component)

    def render(self, indent=0):
        print(' ' * indent + f'{self.title}')
        for child in self.children:
            child.render(indent + 1)

main_menu = MenuGroup("меню сайта")
main_menu.add(MenuItem("главная", '/'))
main_menu.add(MenuItem('о компании', "/about"))

services = MenuGroup("услуги")
services.add(MenuItem("разработка сайтов", "/services/web"))
services.add(MenuItem("мобильные приложения", "/services/mobile"))

main_menu.add(services)
main_menu.add(MenuItem("контакты", "/contacts"))

main_menu.render()

"""
вычислительная система
вложенные
(2+3)*(4-1)
число - лист
операция - компонент

class Expression def evaluate
классы-листья Number
классы-композиты
Addition, Subtraction, Multiplication, Division принимают два дочерних выражения, которые реализуют интерфейс Expression

""" 


from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Number(Expression):
    def __init__(self, value: float):
        self.value = value
    
    def evaluate(self) -> float:
        return self.value
    
    def __str__(self) -> str:
        return str(self.value)

class Addition(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def evaluate(self) -> float:
        return self.left.evaluate() + self.right.evaluate()
    
    def __str__(self) -> str:
        return f"({self.left} + {self.right})"

class Subtraction(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def evaluate(self) -> float:
        return self.left.evaluate() - self.right.evaluate()
    
    def __str__(self) -> str:
        return f"({self.left} - {self.right})"

class Multiplication(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def evaluate(self) -> float:
        return self.left.evaluate() * self.right.evaluate()
    
    def __str__(self) -> str:
        return f"({self.left} * {self.right})"

class Division(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def evaluate(self) -> float:
        divisor = self.right.evaluate()
        if divisor == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return self.left.evaluate() / divisor
    
    def __str__(self) -> str:
        return f"({self.left} / {self.right})"

expr = Multiplication(
    Addition(Number(2), Number(3)),
    Subtraction(Number(4), Number(1))
)
"""
        *
       / \
     +     -
     / \  / \
    2   3 4   1

"""
print(expr.evaluate()) #15