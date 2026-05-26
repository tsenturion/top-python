"""
1502_Сортировки
"""

numbers = [5, 3, 1, 4, 2]


def bubble_sort(array):
    """Сортировка пузырьком: сортирует список на месте."""
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


print('Before:', numbers)
bubble_sort(numbers)
print('After: ', numbers)


def bad_bubble_sort(array):
    """Плохая реализация сортировки пузырьком: неэффективная и медленная."""
    n = len(array)
    for i in range(n):
        for j in range(n):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                
                
print(sorted(numbers))  # O(n log n)