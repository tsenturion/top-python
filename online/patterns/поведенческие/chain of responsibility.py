"""
структура
handler обработчик
concrete handler конкретный обработчик
client клиент
"""

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass

class LowLevelSupport(Handler):
    def handle(self, request):
        if request == 'reset password':
            return "LowLevelSupport: reset password"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "LowLevelSupport не может обработать"

class MidLevelSupport(Handler):
    def handle(self, request):
        if request == 'account blocked':
            return "MidLevelSupport: account blocked"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "MidLevelSupport не может обработать"

class HighLevelSupport(Handler):
    def handle(self, request):
        if request == 'server down':
            return "HighLevelSupport: server down"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "HighLevelSupport не может обработать"

low = LowLevelSupport()
mid = MidLevelSupport()
high = HighLevelSupport()

low.set_next(mid).set_next(high)

print(low.handle("reset password"))
print(low.handle("account blocked"))
print(low.handle("server down"))
print(low.handle("else"))

def handler1(request):
    if request == 'ping':
        return 'pong'
    return None


def handler2(request):
    if request == 'hi':
        return 'hello'
    return None


def chain(request, handlers):
    for handler in handlers:
        result = handler(request)
        if result:
            return result
    return "no handler found"

print(chain('ping', [handler1, handler2]))
print(chain('hi', [handler1, handler2]))
print(chain('bye', [handler1, handler2]))