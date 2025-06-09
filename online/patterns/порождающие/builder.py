from abc import ABC, abstractmethod

#интерфейс строителя
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

#конкретный строитель
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A"

    def build_part_b(self):
        self.product.part_a = "Part B"

    def get_product(self):
        return self.product

#продукт
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None

    def __str__(self):
        return f"Product: part_a={self.part_a}, part_b={self.part_b}"

#директор
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        return self.builder.get_product()

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)
    product = director.construct()
    print(product)