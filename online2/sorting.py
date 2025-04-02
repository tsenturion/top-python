"""
бинарный поиск
"""

"""
по способу организации

внутренняя сортировка - в оперативке
внешняя - для больших данных, с записью во временные файлы
"""

"""
по устойчивости (стабильности)

стабильная сортировка- сохраняет порядок одинаковых элементов
нестабильная - может измениться
"""

"""
по принципу работы

обменные алгоритмы - пузырьковая - if else
выборочные - выбором - выбирается минимальный элемент
вставочные - вставками - новый элемент вставляется в отсортированную часть списка
разделяй и властвуй - быстрая, слиянием - рекурсия, части сортируются
"""

"""
.sort() - сортирует список на месте - изменяет его
sorted() - возвращает новый"""

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
numbers.sort()
print(numbers)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

words = ['123', '1234', '12', '12334']
words.sort(key=len)
print(words)

students = [('иван', 20), ("анна", 18), ("петр", 22)]
students.sort(key=lambda x: x[1])
print(students)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
numbers.sort(reverse=True)
print(numbers)

numbers = [5, 4, 2, 6, 7, 8, 3, 5, 6, 9]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)
"""
O(n)
n - размер входных данных (сколько элементов)
"""

"""
простые O(n^2)
пузырьковая, вставками, выбором
"""

"""
продвинутые O(n log n)
слиянием быстрая 
"""

"""
гибридные
timsort: вставками + слиянием
"""

"""
пузырьковая (bubble sort)
"""

"""
1 проход

[5, 3, 8, 4, 2] 5 3 8 4 2
5 > 3
3 5
[3, 5, 8, 4, 2]
5 < 8
[3, 5, 8, 4, 2]
8 > 4
4 8
[3, 5, 4, 8, 2]
8 > 2
2 8
[3, 5, 4, 2, 8]
"""

def bubble_sort_bad(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#[3, 2, 4, 5, 8]
#[2, 3, 4, 5, 8]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

