"""
стек
deque
lifo
last in, first out
"""

"""

простой способ
list 
.append()
.pop()

правильный 
from collections import deque

"""
from collections import deque
stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

top_element = stack.pop()
top_element2 = stack.pop()
top_element3 = stack.pop()


if stack:
    element = stack.pop()
else:
    print("пуст")
print(top_element)

stack = deque()

"""
push - поместить элемент на вершину .append(element)
pop - снять элемент с вершины 
peek - посмотреть на верхний элемент, не снимая его stack[-1]
"""
if not stack:
    print('стек пуст')

def reverse_string(s):
    stack = deque()
    for char in s:
        stack.append(char)

    reversed_s = ''
    while stack:
        reversed_s += stack.pop()

    return reversed_s

print(reverse_string('hello'))

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return not self.container

    def size(self):
        return len(self.container)


"""
очередь
deque
fifo
first in, first out
"""

"""

простой способ
list 
.append()
.pop(0)

правильный 
from collections import deque

"""
from collections import deque
queue = deque()
queue.append('1')
queue.append('2')
queue.append('3')

first = queue.popleft()
print(first)

"""
enqueue - добавить элемент в конец очереди .append(element)
dequeue - удалить элемент с начала очереди .popleft()
peek - посмотреть на первый элемент, не снимая его stack[0]
"""
if queue:
    first = queue[0]
else:
    print('очередь пуста')

if not queue:
    print("пусто")

size = len(queue)

def serve_customers(customers):
    queue = deque(customers)
    while queue:
        customer = queue.popleft()
        print(f'обслуживается {customer}')

customers_list = ['alice', 'bob', 'joe']
serve_customers(customers_list)

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        return self.container.popleft()

    def peek(self):
        return self.container[0]

    def is_empty(self):
        return not self.container

    def size(self):
        return len(self.container)

q = Queue()
q.enqueue('alice')
q.enqueue('bob')
print(q.dequeue())
print(q.peek())
print(q.size())

"""
deque
double-ended queue
очередь с двумя концами
"""
mydeque = deque()
mydeque.append("A")
mydeque.appendleft("B") # добавление элемента в начало
mydeque.pop()
mydeque.popleft()
"""first_element = mydeque[0]
last_element = mydeque[-1]"""
length = len(mydeque)
if not mydeque:
    print('пусто')
mydeque.clear()

mydeque.extend(['C', "D", 'E']) # добавляет в конец
mydeque.extendleft(["X", "Y"]) # в начало в обратном порядке
mydeque.rotate(1) # все элементы сдвигаются вправо на 1
mydeque.rotate(-1) # все элементы сдвигаются влево на 1

log_queue = deque(maxlen=3)
log_queue.append('log1')
log_queue.append('log2')
log_queue.append('log3')
print(log_queue)
log_queue.append('log4')
print(log_queue)
"""
O()
                    list deque
добавление в конец   1     1
удаление с конца     1     1
добавление в начало  n     1
удаление с начала    n     1
доступ по индексу    1     n
"""

"""
fifi заказы от клиентов
срочный заказ - в начало очереди

add_order(order) - добавить обычный заказ в конец очереди
add_priority_oder(order) - начало
server_order() - обслужить
show_orders() - показать все заказы

учесть пустоту
"""

#from collections import deque

class CafeOrders:
    def __init__(self, max_orders=10):
        self.orders = deque(maxlen=max_orders)

    def add_order(self, order):
        if len(self.orders) == self.orders.maxlen:
            print("очередь полная, невозможно добавить новый заказ")
        else:
            self.orders.append(order)
            print(f"добавлен заказ {order}")

    def add_priority_order(self, order):
        if len(self.orders) == self.orders.maxlen:
            print("очередь полная, невозможно добавить новый заказ")
        else:
            self.orders.appendleft(order)
            print(f"добавлен срочный заказ {order}")

    def serve_order(self):
        if self.orders:
            order = self.orders.popleft()
            print(f"обслуживается заказ {order}")
        else:
            print("нет заказов для обслуживания")

    def show_orders(self):
        if self.orders:
            print("текущие заказы в очереди")
            for order in self.orders:
                print(f"- {order}")

        else:
            print("очередь пуста")

    def clear_orders(self):
        self.orders.clear()
        print("все заказы очищены. кафе закрыто")

    def total_orders(self):
        count = len(self.orders)
        print(f"всего заказов в очереди {count}")
        return count

cafe = CafeOrders(max_orders=5)
cafe.add_order('капучино')
cafe.add_order('латте')
cafe.add_priority_order('эспрессо')
cafe.add_order('американо')
cafe.add_order('кофе')

cafe.show_orders()

cafe.add_order('кофе2')

cafe.serve_order()
cafe.show_orders()

cafe.total_orders()

cafe.clear_orders()
cafe.show_orders()

from abc import ABC, abstractmethod

class OrderQueueStrategy(ABC):
    def __init__(self):
        self.orders = deque()

    @abstractmethod
    def add_order(self, order):
        pass

    @abstractmethod
    def serve_order(self):
        pass

    def show_orders(self):
        for order in self.orders:
            print(f"- {order}")

class PriorityOrderStrategy(OrderQueueStrategy):
    def add_order(self, order):
        self.orders.append(order)
        print(f"добавлен срочный заказ {order}")

    def serve_order(self):
        if self.orders:
            order = self.orders.popleft()
            print(f"обслуживается срочный заказ {order}")
            return order
        return None

class NormalOrderStrategy(OrderQueueStrategy):
    def add_order(self, order):
        self.orders.append(order)
        print(f"добавлен обычный заказ {order}")
        return order

    def serve_order(self):
        if self.orders:
            order = self.orders.popleft()
            print(f"обслуживается обычный заказ {order}")
            return order
        return None

class LowPriorityOrderStrategy(OrderQueueStrategy):
    def add_order(self, order):
        self.orders.append(order)
        print(f"добавлен заказ низкого приоритета{order}")

    def serve_order(self):
        if self.orders:
            order = self.orders.popleft()
            print(f"обслуживается заказ низкого приоритета {order}")
            return order
        return None

class CafeOrderAdvanced:
    def __init__(self):
        self.strategies = {
            0: PriorityOrderStrategy(),
            1: NormalOrderStrategy(),
            2: LowPriorityOrderStrategy()
        }

    def add_order(self, order, priority=1):
        strategy = self.strategies.get(priority)
        if strategy:
            strategy.add_order(order)
        else:
            print(f"неизвестный приоритет {priority} заказ не добавлен")

    def serve_order(self):
        for priority in sorted(self.strategies.keys()):
            order = self.strategies[priority].serve_order()
            if order:
                break
        else:
            print("нет заказов для обслуживания")

    def show_orders(self):
        has_orders = False
        for priority, strategy in sorted(self.strategies.items()):
            if strategy.orders:
                has_orders = True
                match priority:
                    case 0: print("срочные заказы")
                    case 1: print("обычные заказы")
                    case 2: print("заказы низкого приоритета")
                strategy.show_orders()
        if not has_orders:
            print("очередь пуста")


cafe = CafeOrderAdvanced()
cafe.add_order('эспрессо', priority=0)
cafe.add_order('капучино')
cafe.add_order('латте', priority=2)
cafe.add_order('американо')

cafe.show_orders()

cafe.serve_order()
cafe.serve_order()
cafe.serve_order()
cafe.serve_order()
cafe.serve_order()
cafe.serve_order()