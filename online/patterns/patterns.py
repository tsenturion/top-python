# 1 архитектурные паттерны
# 2 паттерны проектирования (23 паттерна)
    # 2.1 порождающие паттерны
    # 2.2 поведенческие паттерны
    # 2.3 структурные паттерны
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

"""
когда используем: (+)

семейство алгоритмов
отделить отправителя запроса от его обработчика
общаться между собой, но не должны быть жестко связаны
"""

"""
не используем: (-)

проблема слишком проста
код и так читаемый и расширяемый
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

# 2.3 структурные паттерны
"""
правильно компоновать объекты 
скрывать сложность 
изолировать части системы 

инкапсуляция сложных структур 
расширение функциональности без изменения кода
переиспользование
снижение связанности 
объединение объектов в более крупные структуры
"""

#adapter
#bridge
#composite
#decorator
#facade
#flyweight
#proxy


"""1. Архитектурные паттерны (уровнем выше, чем GoF)
Это более масштабные подходы к построению систем:

MVVM – для приложений с биндингом данных (чаще в GUI, например, Qt, .NET, мобильные).

Clean Architecture – слоистая архитектура с разделением бизнес-логики, интерфейса и хранилища.

Hexagonal Architecture (Порт-адаптер) – удобна для тестируемых приложений.

Onion Architecture – очень похожа на Clean Architecture.

Microservices – когда каждый модуль — отдельное приложение.

CQRS / Event Sourcing – раздельные подходы к чтению и записи данных.

2. Паттерны интеграции компонентов
(Полезны в распределённых системах и сложных приложениях)

Service Locator

Dependency Injection

Event Bus / Message Bus

Message Queue

API Gateway

Circuit Breaker

Observer + Pub/Sub в сетевом контексте

3. Поведенческие паттерны вне GoF
(Более современные или расширенные формы)

Specification – для сложной бизнес-логики.

Null Object – поведение "ничего не делаю", но без if.

Policy – как альтернатива Strategy.

Middleware (цепочка посредников) – часто используется в веб-фреймворках.

4. Паттерны многопоточности / конкурентности
(Особенно полезно для async / многопоточности)

Thread Pool

Future / Promise

Scheduler

Active Object

Reactor

Producer/Consumer

Monitor / Guarded Suspension

5. Паттерны тестирования
Test Data Builder

Mock / Stub / Spy

Given-When-Then

Arrange-Act-Assert

6. Domain-Driven Design (DDD)
Если хочешь проектировать большие бизнес-приложения, стоит изучить:

Entity, Value Object

Aggregate Root

Repository

Domain Event

Application Layer

Ubiquitous Language

7. Паттерны в базах данных / хранилищах
Active Record

Data Mapper

Repository

Unit of Work

Query Object

8. Паттерны UI/UX / Frontend
(если интересно клиентское приложение)

Virtual DOM

Component / Container

Stateful / Stateless

Slots, Hooks, Refs (если ты уйдёшь в JS / React / Vue и т.п.)

9. Современные подходы и стили проектирования
SOLID-принципы

GRASP-паттерны

KISS, DRY, YAGNI

Refactoring Techniques (каталог Фаулера)

Антипаттерны


Основные протоколы прикладного уровня: 9P, BitTorrent, BOOTP, DNS, FTP, HTTP, NFS;
Основные протоколы прикладного уровня: POP, POP3, SMTP, X.400, X.500, SPDY;
"""
