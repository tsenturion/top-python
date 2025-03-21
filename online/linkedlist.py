#node узел (односвязный)
"""
данные
ссылку на следующий узел
"""

#node узел (двусвязный)
"""
данные
ссылку на следующий узел
ссылка на предыдущий узел
"""

#head голова списка первый узел списка

#tail хвост последний узел списка
"""
может ссылаться на none
может ссылаться на первый элемент (цикл)
"""

1 -> 2 -> 3 -> None

node1
данные: 1
ссылку на следующий узел: -> node2

node2
данные: 2
ссылку на следующий узел: -> node3

node3
данные: 3
ссылку на следующий узел: -> None




node1
данные: 1
ссылку на следующий узел: -> node2

node2
данные: 2
ссылку на следующий узел: -> node3

node3
данные: 3
ссылку на следующий узел: -> node1

singly linked list
1 -> 2 -> 3 -> 4 -> 5 -> None

doubly linked list
None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None

circular linked list
1 -> 2 -> 3 -> 1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]):
        if not head or not head.next:
            return False

        #------
        while head:
            #-----
            head.val
            head = head.next