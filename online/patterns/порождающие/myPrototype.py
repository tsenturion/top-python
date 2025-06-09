"""
прототип - интерфейс с clone()
конкретные прототипы - реализуют clone()
клиент - использует clone()
"""
"""
поверхностное shallow copy()
глубокое копирование deep copy deepcopy()
"""

import copy
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Car(Prototype):
    def __init__(self, model, color, options):
        self.model = model
        self.color = color
        self.options = options

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Car(model={self.model}, color={self.color}, options={self.options})"

if __name__ == "__main__":
    car1 = Car("model", 'color', ['автопилот', "панорамная крыша"])
    print("оригинал", car1)

    car2 = car1.clone()
    car2.color = 'синий'
    car2.options.append("спортивный режим")

    print("копия", car2)
    print("оригинал после клонирования", car1)

