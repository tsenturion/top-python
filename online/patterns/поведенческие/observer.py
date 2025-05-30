"""
структура

subject - интерфейс - издатель - уведомляет observers при изменении своего состояния
observers- подписчики - update() - вызывается при получении уведомления
"""
"""
(+)
отделяет subject observers
можно добавлять observers
нет жесткой зависимости между классами
расширяемость
"""
"""
(-)
производительность при большом количестве подписчиков
подписчики должны правильно удаляться

используем когда
уведомлять другие объекты 
реагируют на изменение состояния объекта
меньше зависимостей
"""

# дополнительно можно import logging
# проблемный код
"""class NewsChannel:
    def __init__(self):
        self.news = ''

    def publish_news(self, news):
        self.news = news
        self.notify_users()

    def notify_users(self):
        print(f"новость {self.news}")

channel = NewsChannel()
channel.publish_news('new')"""

from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} получил уведомление {message}')

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class NewsChannel(Subject):
    def __init__(self):
        self.subscribers = []
        self.news = ''

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news)

    def publish_news(self, news):
        self.news = news
        self.notify()

channel1 = NewsChannel()
user1 = User('alise')
user2 = User('matvey')

channel1.attach(user1)
channel1.attach(user2)

channel1.publish_news('new')

"""
observer
издатель хранит температуру WeatherStation
MobileApp Website - подписчики
при изменении температуры все подписчики обновляются
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class WeatherStation(Subject):
    def __init__(self):
        self.subscribers = []
        self.temperature = 0

    def attach(self, observer):
        self.subscribers.append(observer)

    def detach(self, observer):
        self.subscribers.remove(observer)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self.temperature)

    def set_temperature(self, temperature):
        print(f"новая температура {temperature}")
        self.temperature = temperature
        self.notify()

class MobileApp(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(f"{self.name} получил уведомление {temperature}")

class Website(Observer):
    def update(self, temperature):
        print(f'сайт обновил {temperature}')

weather_station = WeatherStation()

mobile_app1 = MobileApp('приложение 1')
mobile_app2 = MobileApp('приложение 2')
website = Website()

weather_station.attach(mobile_app1)
weather_station.attach(mobile_app2)
weather_station.attach(website)

weather_station.set_temperature(25)
weather_station.set_temperature(30)

weather_station.detach(mobile_app1)

weather_station.set_temperature(20)

"""
чат-комната
ChatRoom - субъект
User - обсервер
пользователь может подписать и отписать от чата в любой момент

Observer
Subject
ChatRoom
User
"""

#from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, message: str):
        pass
    
class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f'{self.name} получил уведомление {message}')
        
class ChatRoom(Subject):
    def __init__(self):
        self._observers = []
        
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)
    
    def add_message(self, message: str):
        print(f'добавлено сообщение {message}')
        self.notify(message)

chat_room = ChatRoom()
user1 = User('alise')
user2 = User('matvey')

chat_room.attach(user1)
chat_room.attach(user2)

chat_room.add_message('hi')
chat_room.detach(user1)
chat_room.add_message('bye')
