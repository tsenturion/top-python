"""
0514_Производительность_list_set_dict
"""

import timeit

time_for_loop = timeit.timeit(
    stmt="""
result = []
for i in range(1000):
    if i % 3 == 3:
        result.append(i)
""",
    number = 10000
)


time_comprehension = timeit.timeit(
    stmt="""
result = [i for i in range(1000) if i % 3 == 3]
""",
    number = 10000
)

print(time_for_loop)
print(time_comprehension)