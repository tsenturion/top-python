"""
дерево
корень root - исходная точка
лист leaf - узлы, без дочерних элементов
глубина узла depth - колво ребер до данного узла
высота дерева height - макс глубина
степень узла degree - количество дочерних узлов у данного узла
потомок child - является потомком
родитель parent - узел, порождает другие узлы


узел - элемент
ребра - связи между узлами
ветви - узлы, с дочерними элементами

бинарное дерево
дерево поиска
дерево отрезков
красно-черное дерево
дерево trie (префиксное)
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#поиск в дереве
def search(root, target):
    if root is None or root.value == target:
        return root
    if target < root.value:
        return search(root.left, target)
    return search(root.right, target)

#вставка элемента
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

#удаление элемента
def delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.legt
        min_larger_node = get_min(root.right)
        root.value = min_larger_node.value
        root.right = delete(root.right, min_larger_node.value)
    return root

#обход дерева
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

"""
граф

вершины (узлы) - объекты
ребра (связи) - связи

ориентированный (направленый) A -> B
неориентированный  A <-> B  A -(5км) B

взвешенные - ребра имеют веса: расстояние, стоимость A -(5км) B
невзвешенные - A - B

представление:
список смежности
graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
}

матрица смежности
graph = [
    [0, 1, 1], #A
    [1, 0, 1], #B
    [1, 1, 0], #C
]
graph[i][j] = 1 #- существует ребро

список ребер
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
]

BFS
"""
#DFS - поиск в глубину
def dfs(graph, start):
    visited = set()
    stack = [start]

    while start:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

#BFS - поиск в ширину
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

#алгоритм Дейкстры

import heapq

def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distance

"""
хеш-таблица или хеш-ассоциативный массив
ключ
значение

хеш-функция
"""

hash_table = [None] * 10

def hash_function(key):
    return len(key) % 10

key = 'apple'
index = hash_function(key)
hash_table[index] = 'яблоко'

"""
хеш-функция
"""

def good_hash_function(key):
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % 10
    return hash_value

"""
коллизии

метод цепочек"""

hash_table = [[] for _ in range(10)]

def insert(key, value):
    index = hash_function(key)
    hash_table[index].append((key, value))

#insert("1", "1")
"""открытая адресация """

def linear_probing_insert(hash_table, key, value):
    index = hash_function(key)
    original_index = index
    while hash_table[index] is not None:
        index = (index + 1) % len(hash_table)
        if index == original_index:
            return
    hash_table[index] = (key, value)

