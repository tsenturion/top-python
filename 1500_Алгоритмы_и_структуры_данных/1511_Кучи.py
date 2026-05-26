"""
1511_Кучи
"""

import heapq

numbers = []

heapq.heappush(numbers, 5)
heapq.heappush(numbers, 3)
heapq.heappush(numbers, 1)
print(heapq.heappop(numbers))  # 1