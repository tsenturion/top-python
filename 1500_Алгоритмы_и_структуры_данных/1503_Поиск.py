"""
1503_Поиск
"""

numbers = [5, 3, 1, 4, 2]

target = 1
for item in numbers:
    if item == target:
        print('Found')
        break # O(n)
    
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7


def binary_search(sorted_list, target):
    """Итеративный бинарный поиск: возвращает индекс target или -1, если не найден."""
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        value = sorted_list[mid]

        if value == target:
            return mid
        if value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


index = binary_search(numbers, target)
if index != -1:
    print(f'Found {target} at index {index}')
else:
    print('Not found')
