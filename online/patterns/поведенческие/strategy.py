"""
гибкого выбора алгоритмов
"""
"""
когда используем (+)

несколько вариантов алгоритма
алгоритмы могут меняться, динамически
без дублирования кода
передавать алгоритм как параметр
"""

"""
когда не используем (-)
статическое переключение алгоритмов

"""
"""
структура

context
strategy interface
concrete strategies
"""

"""
фикс
в зависимости от суммы заказа
для vip
"""

from abc import ABC, abstractmethod

#strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_amount: float) -> float:
        pass

#concrete strategies
class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, total_amount: float) -> float:
        if total_amount > 1000:
            return total_amount * 0.95

class VipDiscount(DiscountStrategy):
    def apply_discount(self, total_amount: float) -> float:
        return total_amount * 0.85

class FixedDiscount(DiscountStrategy):
    def apply_discount(self, total_amount: float) -> float:
        return total_amount * 0.9

#context
class Order:
    def __init__(self, total_amount: float, discount_strategy: DiscountStrategy):
        self.total_amount = total_amount
        self.discount_strategy = discount_strategy

    def get_final_price(self) -> float:
        return self.discount_strategy.apply_discount(self.total_amount)

order1 = Order(1200, FixedDiscount())
order2 = Order(1200, PercentageDiscount())
order3 = Order(1200, VipDiscount())

print(order1.get_final_price())
print(order2.get_final_price())
print(order3.get_final_price())


"""
альтернатива
"""

def fixed_discount(amount):
    return amount * 0.9

def vip_discount(amount):
    return amount * 0.85

def percentage_discount(amount):
    return amount * 0.95 if amount > 1000 else amount

class Order:
    def __init__(self, total_amount: float, discount_function):
        self.total_amount = total_amount
        self.discount_function = discount_function

    def get_final_price(self) -> float:
        return self.discount_function(self.total_amount)

order1 = Order(1200, fixed_discount)
order2 = Order(1200, percentage_discount)
order3 = Order(1200, vip_discount)

print(order1.get_final_price())
print(order2.get_final_price())
print(order3.get_final_price())

"""
Strategy
расчет стоимости доставки

обычная доставка с фиксированной ценой
экспресс доставка с ценой выше
самовывоз бесплатный
"""

from abc import ABC, abstractmethod

#интерфейс стратегии
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass

#конкретные стратегии
class StandardDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 200

class ExpressDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 200 + weight * 50

class Pickup(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return 0

#контекст
class Order:
    def __init__(self, weight: float, delivery_strategy: DeliveryStrategy):
        self.weight = weight
        self.delivery_strategy = delivery_strategy

    def get_delivery_price(self) -> float:
        return self.delivery_strategy.calculate_cost(self.weight)

order1 = Order(2, StandardDelivery())
order2 = Order(2, ExpressDelivery())
order3 = Order(2, Pickup())

print(order1.get_delivery_price())
print(order2.get_delivery_price())
print(order3.get_delivery_price())

"""
платежная система

банковская карта
электронный кошелек
криптовалюта

Создайте интерфейс стратегии PaymentStrategy с методов pay(amount: float)
Реализуйте три класса-стратегии:

CreditCardPayment
EWalletPayment
CryptoPayment

Релизуйте класс Order, который будет использовать объект стратегии для выполнения оплаты
"""
#from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Платеж на сумму {amount} через банковскую карту выполнен")

class EWalletPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Платеж на сумму {amount} через электронный кошелек выполнен")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Платеж на сумму {amount} через криптовалюту выполнен")

class Order:
    def __init__(self, amount: float, strategy: PaymentStrategy) -> None:
        self.amount = amount
        self.strategy = strategy

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.strategy = strategy

    def proces_order(self) -> None:
        print(f"Обработка заказа на сумму {self.amount}")
        self.strategy.pay(self.amount)

order = Order(1000, CreditCardPayment())
order.proces_order()

order.set_payment_strategy(EWalletPayment())
order.proces_order()