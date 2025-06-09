from abc import ABC, abstractmethod

#продукт

class Car:
    def __init__(self):
        self.model = None
        self.engine = None
        self.color = "белый"
        self.options = []
    
    def __str__(self):
        return (
            f"Автомобиль: {self.model}\n"
            f"Двигатель: {self.engine}\n"
            f"цвет: {self.color}\n"
            f"Опции: {', '.join(self.options) or 'нет'}"
        )
    
#интерфейс строителя
class CarBuilder(ABC):
    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    def set_color(self, color):
        pass

    def add_option(self, option):
        pass

    @abstractmethod
    def get_car(self):
        pass

#конкретные строители

class BasicCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()
    
    def set_model(self):
        self.car.model = "Базовый автомобиль"
    
    def set_engine(self):
        self.car.engine = "Базовый двигатель"
    
    def set_color(self, color):
        self.car.color = color
    
    def add_option(self, option):
        if option not in self.car.options:
            self.car.options.append(option)

    def get_car(self):
        return self.car

class PremiumCarBuilder(BasicCarBuilder):
    def set_model(self):
        self.car.model = "Превиум автомобиль"

    def set_engine(self):
        self.car.engine = "Превиум двигатель"
    

#директор
class Director:
    def construct_sport_car(self, builder):
        builder.set_model()
        builder.set_engine()
        builder.set_color("синий")
        builder.add_option("автоматическая коробка")
        builder.add_option("автоматический парктроник")
        builder.add_option("автоматический климат")
        return builder.get_car()
    
    def construct_family_car(self, builder):
        builder.set_model()
        builder.set_engine()
        builder.set_color("черный")
        builder.add_option("полный капот")
        builder.add_option("автоматическая коробка")
        builder.add_option("автоматический парктроник")
        builder.add_option("автоматический климат")
        return builder.get_car()
    
#протестировать

director = Director()
sport_car_builder = PremiumCarBuilder()
family_car_builder = BasicCarBuilder()

family_car = director.construct_family_car(family_car_builder)

print(family_car)

sport_car = director.construct_sport_car(sport_car_builder)

print(sport_car)




    
