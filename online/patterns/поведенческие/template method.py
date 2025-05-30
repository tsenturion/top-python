"""
определяет общий алгоритм
изменение отдельных шагов
"""
"""
структура:
basic базовый класс, с prepare()
в prepare() другие методы с возможностью переопределения
concrete подклассы переопределяют только нужное

(+)
избегает дублирования кода 
SRP
OCP

(-)
Если алгоритм слишком сложный, может быть сложно выделить общий алгоритм
подклассы жестко привязаны к основному классу
"""
#проблемный вариант
"""class Tea:
    def prepare(self):
        print("кипятим")
        print("чай")
        print("сахар")
        print("в кружку")

class Coffee:
    def prepare(self):
        print("кипятим")
        print("кофе")
        print("молоко")
        print("в кружку")
        
tea = Tea()
tea.prepare()

coffee = Coffee()
coffee.prepare()"""

from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.add_condiments()
        self.pour()

    def boil_water(self):
        print("кипятим")

    def pour(self):
        print("в кружку")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):
        print("чай")

    def add_condiments(self):
        print("сахар")

class Coffee(Beverage):
    def brew(self):
        print("кофе")

    def add_condiments(self):
        print("молоко")

tea = Tea()
tea.prepare()

print('---------')

coffee = Coffee()
coffee.prepare()


"""
добавить новый класс
HotChocolate(Beverage):
"""

"""
базовый класс DataProcessor - алгоритм обработки данных

загрузка данных load_data
обработка process_data
сохранение save_data

два подкласса с разными форматами (csv/txt/json...)
CSVProcessor и TextProcessor с process()
"""

from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def process(self):
        data = self.load_data()
        process_data = self.process_data(data)
        self.save_data(process_data)

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def save_data(self, data):
        pass

class CSVProcessor(DataProcessor):
    def load_data(self):
        print(f"загрузка из {self.input_file}")
        with open(self.input_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def process_data(self, data):
        print("обработка из CSV")
        return [{"name": row[0], 'count': int(row[1])} for row in data]

    def save_data(self, data):
        print(f"сохранение в {self.output_file}")
        with open(self.output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


class TextProcessor(DataProcessor):
    def load_data(self):
        print(f"загрузка {self.input_file}")
        with open(self.input_file, 'r', encoding='utf-8') as file:
            return file.read()

    def process_data(self, data):
        print('обработка текста')
        return data.upper()

    def save_data(self, data):
        print(f'сохранение в {self.output_file}')
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(data)

csv_processor = CSVProcessor('data.csv', "data.json")
csv_processor.process()

print("------------")

text_processor = TextProcessor('text.txt', 'text_processed.txt')
text_processor.process()

"""
data.csv

apple,10
banana,5
orange,7
"""
"""
text.txt

ewveefv
"""