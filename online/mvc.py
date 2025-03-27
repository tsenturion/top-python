# 1 архитектурные паттерны
# 2 паттерны проектирования
    # 2.1 порождающие паттерны
    # 2.2 поведенческие паттерны
# 3 идиомы

# mvc model view controller (1)
"""
model
управление данными/бизнес логика
хранение/извлечение/обработка данных
ORM

view
отображение
html/css/js
получаем данные от модели через контроллер

controller
управляет взаимодействием между моделью и представлением
http


"""
"""
разделение ответственности
модульность
масштабируемость
тестируемость
гибкость
упрощение разработки
"""

#ORM
"""
(фреймворки)
django
flask

pyramid
"""
"""
/src
    -контроллеры
    -модели
    -представления
    -core           - классы для управления MVC
    -config.py      - конфигурация приложения
    -Main.py        - точка входа в приложение 
"""

#порождающие паттерны

# Singleton
# Builder
# Factory Method
# Abstract Factory
# Prototype

# Builder
"""
создаем сложные объекты пошагово, когда есть параметры/несколько этапов
"""
"""
builder 
интерфейс строителя 
абстрактный интерфейс

concrete builders
конкретные строители 
реализуют builder

product
наш сложный объект

director
управление, порядок вызова методов строителя, строителей
"""

# Factory Method
"""
Creator
ConcreteCreator
Product
ConcreteProduct
"""

# 2.2 поведенческие паттерны
"""
инкапсуляция 
передача ответственности
ослабление связей
"""

"""
виды

управления алгоритмами
коммуникации между объектами
управления состоянием
"""
#управления алгоритмами
"""
strategy
interpreter 
visitor 

template method
"""

#коммуникации между объектами
"""
observer 
mediator 
command 
iterator

chain of responsibility 
protocol
"""

#управления состоянием
"""
state
memento 
"""