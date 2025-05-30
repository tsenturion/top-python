"""
структура
интерфейс посредника - управляет взаимодействием
конкретный класс - логика общения
компоненты - запросы посреднику

используем когда
между объектами много взаимодействий
много компонентов, между которыми много взаимодействий
хотим упростить

при использовании паттерна
есть централизованный объект, управляющий взаимодействием между объектами
каждый объект знает только посредника, а не всех других объектов
"""
"""
(+)
уменьшает зависимость между объектами

(-)

"""
#проблемыный код
"""class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, message, user):
        print(f"{self.name} отправляет сообщение {user.name}: {message}")

alice = User("alice")
bob = User("bob")

alice.send_message("hi", bob)
bob.send_message("hi", alice)"""

from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive_massage(message, sender)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send_message(self, message):
        print(f"{self.name} отправляет сообщение {message}")
        self.mediator.send_message(message, self)

    def receive_massage(self, message, sender):
        print(f'{self.name} получил сообщение от {sender.name} {message}')

chat = ChatRoom()

alice = User("alice", chat)
bob = User("bob", chat)
matvey = User('matvey', chat)

alice.send_message('hi')
bob.send_message('hi')



"""
mediator
реализовать чат

разные роли + модерация сообщений:

user - может отправлять сообщения
moderator - может удалять
admin - может блокировать пользователей

ChatRoom управляет всеми пользователями и сообщениями

модерация сообщений:
ban_word_list = ['слово', "еще"]

блокировка пользователей:
админ - может заблокировать пользователей
"""
from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, sender):
        pass

    @abstractmethod
    def remove_message(self, message, moderator):
        pass

    @abstractmethod
    def block_user(self, user, admin):
        pass

class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []
        self.banned_users = set()
        self.messages = []
        self.ban_word_list = {"спам", "оскорбление"}

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        if sender in self.banned_users:
            print(f"{sender.name} заблокирован и не может отправлять сообщения.")
            return

        if any(word in message.lower() for word in self.ban_word_list):
            print(f"Сообщение от {sender.name} содержит запрещенные слова и не отправлено.")
            return

        self.messages.append((sender, message))
        for user in self.users:
            if user != sender:
                user.receive_message(message, sender)

    def remove_message(self, message, moderator):
        for msg in self.messages:
            if msg[1] == message:
                self.messages.remove(msg)
                print(f"Модератор {moderator.name} удалил сообщение: {message}")
                return
        print(f"Сообщение не найдено.")

    def block_user(self, user, admin):
        self.banned_users.add(user)
        print(f"Админ {admin.name} заблокировал пользователя {user.name}.")

class User(ABC):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    @abstractmethod
    def send_message(self, message):
        pass

    def receive_message(self, message, sender):
        print(f"{self.name} получил сообщение от {sender.name}: {message}")

class RegularUser(User):
    def send_message(self, message):
        print(f"{self.name} отправил сообщение: {message}")
        self.mediator.send_message(message, self)

class Moderator(User):
    def send_message(self, message):
        print(f"{self.name} (Модератор) отправил сообщение: {message}")
        self.mediator.send_message(message, self)

    def remove_message(self, message):
        self.mediator.remove_message(message, self)

class Admin(User):
    def send_message(self, message):
        print(f"{self.name} (Админ) отправил сообщение: {message}")
        self.mediator.send_message(message, self)

    def block_user(self, user):
        self.mediator.block_user(user, self)

chat = ChatRoom()

alice = RegularUser("Алиса", chat)
bob = RegularUser("Боб", chat)
charlie = Moderator("Чарли", chat)
diana = Admin("Диана", chat)

alice.send_message("Всем привет!")
bob.send_message("Привет, Алиса!")
charlie.send_message("Я буду следить за порядком.")
alice.send_message("Оскорбление!")

charlie.remove_message("Оскорбление!")

diana.block_user(bob)

bob.send_message("Я еще здесь!")


"""
mediator
умный дом

умный будильник
умная кофеварка
умные шторы
аудиосистема
освещение

при срабатывании будильника:
открыть шторы
завести кофеварку
включить свет
включить музыку

центральный посредник mediator - управляет всеми устройствами

интерфейс SmartDevice:
класс HomeMediator - посредник

классы устройств:
AlarmClock
CoffeeMachine
Curtains
Lights
AudioSystem

AlarmClock.trigger() -> включает свет, открывает шторы, включает кофеварку и музыку
"""

#from abc import ABC, abstractmethod
from typing import Any

class Mediator:
    @abstractmethod
    def notify(self, sender: Any, event: str) -> None:
        pass

class SmartDevice(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

class HomeMediator(Mediator):
    def __init__(self):
        self.alarm_clock = None
        self.coffee_machine = None
        self.curtains = None
        self.lights = None
        self.audio_system = None

    def notify(self, sender: Any, event: str) -> None:
        if isinstance(sender, AlarmClock) and event == "wake_up":
            print("[Mediator]Событие: Будильник сработал!")
            self.curtains.open()
            self.lights.turn_on()
            self.coffee_machine.brew()
            self.audio_system.play_music()

class AlarmClock(SmartDevice):
    def trigger(self):
        print("[AlarmClock]Будильник сработал!")
        self.mediator.notify(self, "wake_up")

class CoffeeMachine(SmartDevice):
    def brew(self):
        print("[CoffeeMachine]Кофе готово!")

class Curtains(SmartDevice):
    def open(self):
        print("[Curtains]Шторы открыты!")

class Lights(SmartDevice):
    def turn_on(self):
        print("[Lights]Свет включен!")

class AudioSystem(SmartDevice):
    def play_music(self):
        print("[AudioSystem]Музыка проигрывается!")


mediator = HomeMediator()

alarm = AlarmClock(mediator)
coffee = CoffeeMachine(mediator)
curtains = Curtains(mediator)
lights = Lights(mediator)
audio = AudioSystem(mediator)

mediator.alarm_clock = alarm
mediator.coffee_machine = coffee
mediator.curtains = curtains
mediator.lights = lights
mediator.audio_system = audio

alarm.trigger()