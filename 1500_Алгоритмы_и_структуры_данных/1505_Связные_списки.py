"""
1505_Связные_списки
"""
"""
односвязные списки
двусвязные
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2) 
node3 = Node(3)

node1.next = node2
node2.next = node3

# 1 -> 2 -> 3 -> None
# numbers[500] O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# None <- 1 <-> 2 <-> 3 -> None
