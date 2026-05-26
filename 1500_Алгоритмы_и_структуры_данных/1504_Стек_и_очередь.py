"""
1504_Стек_и_очередь
"""

stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2


"""
Очередь - это структура данных, которая работает по принципу "первый пришел - первый ушел" (FIFO).

обычная очередь
очередь с приоритетом
двусторонняя очередь (deque)
"""

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # 1