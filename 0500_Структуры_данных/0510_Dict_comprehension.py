"""
0510_Dict_comprehension
"""

dict_comp = {
    x: x * x
    for x in range(5)
    if x % 2 == 0
}
print(dict_comp)