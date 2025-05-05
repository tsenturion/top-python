"""
односвязный список
value/val/data - данные/значение
ptr/next - ссылка на следующий элемент/узел

self.next
self.prev
1 -> 2 -> 3 -> None

[значение|ссылка на следующий] -> [значение|ссылка на следующий] -> [значение|None]

None - узел
head - голова списка (начало - начальный элемент)

добавление элемента в начало списка
добавление элемента в конец списка
удаление элемента
поиск элемента по названию
вывод всех элементов списка
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_value(self, key):
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if not current:
            print("элемент не найден")
            return

        if not previous:
            self.head = current.next
        else:
            previous.next = current.next

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return current

    def insert_after(self, target_value, new_data):
        current = self.head
        while current and current.data != target_value:
            current = current.next

        if not current:
            return

        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def clear(self):
        self.head = None

"""
двусвязный список
циклический список
упорядоченный список
"""

"""
хорошие практики

head is None проверка пустой ли список
current.next is None проверка конца списка
аккуратны при удалении головы
не теряем ссылки на оставшуюся часть при изменениях
"""

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# обход списка
current = head
while current:
    print(current.val)
    current = current.next

#подсчет длины списка
length = 0
current = head
while current:
    length += 1
    current = current.next

#поиск узла по значению
target = 7
current = head
while current:
    if current.val == target:
        print("найдено")
        break
    current = current.next


#вставка нового узла после заданного значения
new_node = ListNode(99)
current = head
while current:
    if current.val == 5:
        new_node.next = current.next
        current.next = new_node
        break
    current = current.next

#удаление узла по значению (без головы списка)
target = 3
current = head
prev = None

while current:
    if current.val == target:
        if prev:
            prev.next = current.next
        else:
            head = current.next
        break
    prev = current
    current = current.next

#разворот односвязного списка (reverse). Три указателя prev current next_node
prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

head = prev

#поиск середины списка (быстрый и медленный указатель)
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print('середина', slow.val)

#обнаружение цикла (алгоритм флойда)
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print("цикл обнаружен")
        break

#доступ к N-му элементу (по индексу)
index = 4
i = 0
current = head

while current and i < index:
    current = current.next
    i += 1

if current:
    print("значение", current.val)
else:
    print('индекс вне диапазона')

#сравнение двух списков (на равенство)
def are_equal(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return l1 is None and l2 is None

#очистка списка (если нужно вручную)
current = head
while current:
    next_node = current.next
    del current
    current = next_node
head = None

