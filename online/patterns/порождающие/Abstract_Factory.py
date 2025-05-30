"""
абстрактная фабрика - интерфейс/ABC cls, набор методов для создания объектов
конкретные фабрики - реализуют абстрактную фабрику
абстрактные продукты - интерфейс/ABC cls, определяют общее поведение объектов
конкретные продукты - реализуют абстрактные продукты
клиентский код - использует фабрику, работает с интерфейсами
"""

#абстрактная фабрика
from abc import ABC, abstractmethod

class GUTFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

#конкретные фабрики
class WindowFactory(GUTFactory):
    def create_button(self):
        return WindowButton()

    def create_checkbox(self):
        return WindowCheckbox()

class MacOSFactory(GUTFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSChecbox()

#абстрактные продукты

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

#конкретные продукты

class WindowButton(Button):
    def render(self):
        return "отрисовка Button в win"

class WindowCheckbox(Checkbox):
    def render(self):
        return "отрисовка Checkbox в win"

class MacOSButton(Button):
    def render(self):
        return "отрисовка Button в MacOS"

class MacOSChecbox(Checkbox):
    def render(self):
        return "отрисовка Checkbox в MacOS"

#клиентский код

def create_ui(factory: GUTFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.render())
    print(checkbox.render())

os_type = "Windows"

if os_type == "Windows":
    factory = WindowFactory()
else:
    factory = MacOSFactory()

