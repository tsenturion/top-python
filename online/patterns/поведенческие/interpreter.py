#interpreter
"""
разбираем и вычисляем выражения разного языка
"""
"""
причины использования

предметная область
простая ограниченная грамматика
легко добавлять новые операции
"""

"""
нет

очень сложный
большое количество правил
редко меняются
"""

"""
структура

expression
concrete expressions
context
"""

# 2 + 3 * 4

from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass

class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value

class Addition(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()

class Multiplication(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() * self.right.interpret()

class Subtraction(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()


expr = Addition(Number(2), Multiplication(Number(3), Number(4)))

result = expr.interpret()
print(result)

expr2 = Subtraction(Number(10), Addition(Number(2), Number(3)))

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y
}

def interpret(expression: str) -> int:
    tokens = expression.split()
    left, op, right = int(tokens[0]), tokens[1], int(tokens[2])
    return operations[op](left, right)

print(interpret("2 + 3"))

"""
interpreter

ON - включить свет
OFF
STATUS - показать текущее состояние

input
"""

from abc import ABC, abstractmethod

#интерфейс команды

class Command(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

#команды
class TurnOnCommand(Command):
    def interpret(self, context):
        context["light"] = "ON"
        print("свет вкл")

class TurnOffCommand(Command):
    def interpret(self, context):
        context["light"] = "OFF"
        print("свет выкл")

class StatucCommand(Command):
    def interpret(self, context):
        print(f"сейчас {context['light']}")

class CommandFactory:
    commands = {
        'ON': TurnOnCommand,
        'OFF': TurnOffCommand,
        'STATUS': StatucCommand
    }

    @staticmethod
    def get_command(command_name):
        return CommandFactory.commands.get(command_name, None)

def main():
    context = {'light': 'OFF'}
    while True:
        command_name = input().strip().upper()
        if command_name == 'EXIT':
            print("выход")
            break

        command_class = CommandFactory.get_command(command_name)
        if command_class:
            command = command_class()
            command.interpret(context)
        else:
            print("неверн ком")

if __name__ == "__main__":
    main()


"""
пользователь может быть описан полями
role: строка ('admin', 'user')
active: логическое (true, false)

фильтры описываются:
"role == admin" 
"active == true"
"role == admin AND active == true"
"role == user OR active == false"
"""

user1 = {'role': 'admin', 'active': True}
user2 = {'role': 'user', 'active': False}

from abc import ABC, abstractmethod


# Абстрактный класс для всех выражений
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict) -> bool:
        pass


# Конкретные выражения
class EqualsExpression(Expression):
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value.lower()

    def interpret(self, context: dict) -> bool:
        context_value = str(context.get(self.key)).lower()
        return context_value == self.value


class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: dict) -> bool:
        return self.expr1.interpret(context) and self.expr2.interpret(context)


class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: dict) -> bool:
        return self.expr1.interpret(context) or self.expr2.interpret(context)


def parse(expression_str: str) -> Expression:
    tokens = expression_str.split()

    def parse_equals(token1, token2, token3):
        if token2 != "==":
            raise ValueError("Ожидался оператор ==")
        return EqualsExpression(token1, token3)

    i = 0
    current_expr = None

    while i < len(tokens):
        if tokens[i + 1] == "==":
            left = parse_equals(tokens[i], tokens[i + 1], tokens[i + 2])
            i += 3

            if i < len(tokens):
                op = tokens[i]
                i += 1
                right = parse_equals(tokens[i], tokens[i + 1], tokens[i + 2])
                i += 3

                if op == "AND":
                    current_expr = AndExpression(left, right)
                elif op == "OR":
                    current_expr = OrExpression(left, right)
                else:
                    raise ValueError(f"Неизвестный логический оператор: {op}")
            else:
                current_expr = left
        else:
            raise ValueError("Неверный формат фильтра")

    return current_expr


if __name__ == "__main__":
    user1 = {"role": "admin", "active": True}
    user2 = {"role": "user", "active": False}

    expressions = [
        "role == admin",
        "active == false",
        "role == user OR active == true",
        "role == admin AND active == true"
    ]

    for expr_str in expressions:
        expr = parse(expr_str)
        print(f"Выражение: {expr_str}")
        print(f"user1: {expr.interpret(user1)}")
        print(f"user2: {expr.interpret(user2)}")
        print("-" * 30)
