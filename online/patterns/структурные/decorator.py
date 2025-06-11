"""
структура:
component компонент
concreteComponent
Decorator декоратор
concreteDecorator конкретный декоратор

Client -> Decorator1 -> Decorator2 -> ... -> ConcreteComponent

применяем когда:
расширяет функционал не изменяя код 
необходимость добавления дополнительного функционала во множество объектов
отделить основный функционал от дополнительного


@functools.lru_cache
@staticmethod
@login_required

(-)
увеливает количество классов
может быть сложно понять стек оберток
иногда проще наследование или функции


adapter меняет интерфейс
proxy тоже обораивает, но для контроля доступа или отложенной загрузки
composite строит иерархии 
"""
class MessageSender:
    def send(self, message: str):
        raise NotImplementedError

class SimpleSender(MessageSender):
    def send(self, message: str):
        print(f"sending {message}")

class SenderDecorator(MessageSender):
    def __init__(self, wrappee: MessageSender):
        self._wrappee = wrappee

    def send(self, message: str):
        self._wrappee.send(message)

class EncryptedSender(SenderDecorator):
    def send(self, message: str):
        encrypted = self._encrypt(message)
        print('encr')
        self._wrappee.send(encrypted)

    def _encrypt(self, text):
        return ''.join(chr(ord(c) + 1) for c in text)

class LoggingSender(SenderDecorator):
    def send(self, message: str):
        print(f"[LOG] {message}")
        self._wrappee.send(message)

base = SimpleSender()
logged = LoggingSender(base)
secure = EncryptedSender(logged)

secure.send("hi")

"""
decorator
выводить текст, оборачивая его
    жирный
    курсив
    зачеркнут
TextComponent render() - просто возвращает строку
PlainText - просто текст
    BoldDecorator **текст**
    курсивdecorator *текст*
    зачеркнутdecorator ~~текст~~
"""

class TextComponent:
    def render(self) -> str:
        raise NotImplementedError

class PlainText(TextComponent):
    def __init__(self, text: str):
        self.text= text

    def render(self) -> str:
        return self.text

class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self._component = component

    def render(self) -> str:
        return self._component.render()

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"**{super().render()}**"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"*{super().render()}*"

class StrikethroughDecorator(TextDecorator):
    def render(self) -> str:
        return f"~~{super().render()}~~"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"__{super().render()}__"

base = PlainText("hi")
decorated = ItalicDecorator(BoldDecorator(StrikethroughDecorator(base)))
print(decorated.render())

"""
система расчета стоимости билетов
у билета базовая цена
    vip
    страховка
    срочная покупка
к цене добавляются надбавки

интерфейс Ticket
class BaseTicket
    get_price
    get_description

декораторы-наценки
наследуются от интерфейса Ticket с ссылкой на объект Ticket
VipAccessDecorator - цена * 1.5 с вип доступом
InsuranceDecorator - цена + 100 со страховкой
LastMinuteDecorator - цена * 1.3 за срочную покупку
"""

from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

class BaseTicket(Ticket):
    def __init__(self, base_price: float):
        self.base_price = base_price

    def get_price(self) -> float:
        return self.base_price

    def get_description(self) -> str:
        return f"Base price: {self.base_price}"

class TicketDecorator(Ticket):
    def __init__(self, wrapped_ticket: Ticket):
        self.wrapped_ticket = wrapped_ticket

    def get_price(self) -> float:
        return self.wrapped_ticket.get_price()

    def get_description(self) -> str:
        return self.wrapped_ticket.get_description

class VipAccessDecorator(TicketDecorator):
    def get_price(self) -> float:
        return self.wrapped_ticket.get_price() * 1.5

    def get_description(self) -> str:
        return f"{self.wrapped_ticket.get_description()}, VIP access"

class InsuranceDecorator(TicketDecorator):
    def get_price(self) -> float:
        return self.wrapped_ticket.get_price() + 100

    def get_description(self) -> str:
        return f"{self.wrapped_ticket.get_description()}, Insurance"

class LastMinuteDecorator(TicketDecorator):
    def get_price(self) -> float:
        return self.wrapped_ticket.get_price() * 1.3

    def get_description(self) -> str:
        return f"{self.wrapped_ticket.get_description()}, Last minute"

ticket = BaseTicket(base_price=100)
ticket = VipAccessDecorator(ticket)
ticket = InsuranceDecorator(ticket)
ticket = LastMinuteDecorator(ticket)

print(f"Price: {ticket.get_price()}")
print(f"Description: {ticket.get_description()}")