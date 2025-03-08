import PyQt5.QtDesigner

import pickle

#data = {'name': "alice", 'age': 24, 'city': 'new york'}

class Person:
    health = 100
    @classmethod
    def print_health(cls):
        print(cls.health)

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.__gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

    def __str__(self):
        return f"Person name={self.name}, age={self.age}"

person = Person("alice", 24)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

with open('person.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

"""
Задание 1
Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицы в качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку).
"""

class CountryCapitalDatabase:
    def __init__(self, filename='data.pkl'):
        self.filename = filename
        self.data = self.load_data()

    def add_country(self, country, capital):
        self.data[country] = capital
        print(f"Добавлено: {country} - {capital}")

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f"Удалено: {country}")
        else:
            print(f"Страна {country} не найдена")

    def search_country(self, country):
        return self.data.get(country, "Страна не найдена")

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            print(f"Обновлено: {country} - {new_capital}")
        else:
            print(f"Страна {country} не найдена")

    def save_data(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.data, file)
        print("Данные сохранены")

    def load_data(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return {}

    def display_data(self):
        if self.data:
            for country, capital in self.data.items():
                print(f"{country}: {capital}")
        else:
            print("База данных пуста")


db = CountryCapitalDatabase()

db.add_country('Россия', "Москва")
db.add_country('Россия2', "Москва")
db.display_data()

db.edit_country('Россия2', "Москва2")
db.display_data()

db.remove_country('Россия2')
db.display_data()

db.search_country('Россия')
db.search_country('Россия2')

db.save_data()
"""
Задание 2
Есть некоторый словарь, который хранит названия
музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
альбомов в качестве значения. Необходимо реализовать:
добавление данных, удаление данных, поиск данных,
редактирование данных, сохранение и загрузку данных
(используя упаковку и распаковку)."""

import random
a = tuple([{"1": "13"}, ])
print(a)
print(random.sample(list({"ключ": "значение",
                          'b': 2,
                          "c": 3}
                         .keys()), 2))