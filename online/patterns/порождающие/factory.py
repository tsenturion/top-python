from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        print("drive sedan")

class SUV(Car):
    def drive(self):
        print("drive SUV")

class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

class SedanFactory(CarFactory):
    def create_car(self) -> Car:
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self) -> Car:
        return SUV()


def get_car(factory: CarFactory):
    car = factory.create_car()
    car.drive()

sedan_factory = SedanFactory()
get_car(sedan_factory)

suv_factory = SUVFactory()
get_car(suv_factory)