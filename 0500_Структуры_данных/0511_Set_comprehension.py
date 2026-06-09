"""
0511_Set_comprehension
"""

text = 'Hello Python World'
set_comp = {
    char.upper()
    for char in text 
    if char != ' '
}
print(set_comp)