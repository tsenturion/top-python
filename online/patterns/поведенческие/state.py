"""
структура
context - контекст - основной
state interface - базовое состояние
concrete states - конкретные состояния

преимущества
изоляция поведения 
упрощение кода
гибкость
расширяемость

отличия от strategy
state - динамика
strategy - внешнее
"""


from abc import ABC, abstractmethod

class EditorState(ABC):
    @abstractmethod
    def type_char(self, context, char: str):
        pass

"""class InsertState(EditorState):
    def type_char(self, context, char: str):
        context.text = context.text[:context.cursor] + char + context.text[context.cursor:]
        context.cursor += 1
        print(f'[Insert] {context.text}')
"""
class OverwriteState(EditorState):
    def type_char(self, context, char: str):
        if context.cursor < len(context.text):
            context.text = context.text[:context.cursor] + char + context.text[context.cursor + 1:]
        else:
            context.text += char
        context.cursor += 1
        print(f"[Overwrite] {context.text}")


class TextEditor:
    def __init__(self):
        self.text = ''
        self.cursor = 0
        self._state: EditorState = InsertState()

    def set_state(self, state: EditorState):
        self._state = state

    def type_char(self, char: str):
        self._state.type_char(self, char)

class InsertState(EditorState):
    def type_char(self, context, char: str):
        if char == "#":
            context.set_state(OverwriteState())
            print("переход в OverwriteState")
        else:
            context.text = context.text[:context.cursor] + char + context.text[context.cursor:]
            context.cursor += 1

editor = TextEditor()
editor.type_char("H")
editor.type_char("e")
editor.type_char("l")
editor.type_char("l")
editor.type_char("o")

editor.cursor = 0
editor.set_state(OverwriteState())
editor.type_char("h")
editor.type_char("i")

"""state = {
    "insert": insert_func,
    "overwrite": overwrite_func
}"""

"""
state
чат
пользователь - гость/авторизован/модератор
"""

from abc import ABC, abstractmethod

class UserState(ABC):
    @abstractmethod
    def view_messages(self, context):
        pass

    @abstractmethod
    def send_message(self, context, message: str):
        pass

    @abstractmethod
    def delete_message(self, context, message_id: int):
        pass

class GuestState(UserState):
    def view_messages(self, context):
        print("гость смотрит")

    def send_message(self, context, message: str):
        print('гость не может отправить')

    def delete_message(self, context, message_id: int):
        print('гость не может удалить')

class AuthenticatedState(UserState):
    def view_messages(self, context):
        print("пользователь смотрит")

    def send_message(self, context, message: str):
        print(f'пользователь отправил {message}')

    def delete_message(self, context, message_id: int):
        print('пользователь не может удалить')

class ModeratorState(UserState):
    def view_messages(self, context):
        print("модератор смотрит")

    def send_message(self, context, message: str):
        print(f'модератор отправил {message}')

    def delete_message(self, context, message_id: int):
        print(f'модератор удалил сообщение с id {message_id}')

class User:
    def __init__(self):
        self._state: UserState = GuestState()

    def set_state(self, state: UserState):
        self._state = state
        print(f"состояние стало {type(state).__name__}")

    def view_messages(self):
        self._state.view_messages(self)

    def send_message(self, message: str):
        self._state.send_message(self, message)

    def delete_message(self, message_id: int):
        self._state.delete_message(self, message_id)


user = User()
user.view_messages()
user.send_message('hi')
user.delete_message(1)

user.set_state(AuthenticatedState())
user.view_messages()
user.send_message('hii')
user.delete_message(1)

user.set_state(ModeratorState())
user.view_messages()
user.send_message('hiii')
user.delete_message(1)

"""
банкомат/банковская карта

активна
заблокирована
истек срок действия

Satate 

оплата покупки
пополнение баланса
проверка баланса
блок/анлок карты

Сосотояния
ActiveState - нормально работает
BlockedState - нельзя совершать операции
ExpiredState - можно смотреть баланс
InactiveState - карта еще не активирована

CardState
pay(amount)
top_up(amount)
check_balance()
block()
unblock()

BankCard
хранит баланс
ссылку на текущее состояние state
методы делегируют действия текущему состоянию
"""