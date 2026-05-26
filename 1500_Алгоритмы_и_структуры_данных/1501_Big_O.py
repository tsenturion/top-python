"""
1501_Big_O
"""

numbers = [1, 2, 3, 4, 5]
# print(numbers[0])  # O(1)
# numbers.pop(0)  # O(n)
numbers.append(6)  # O(1)


# for item in numbers:
#     print(item)  # O(n)
    
for i in numbers:
    for j in numbers:
        print(i, j)  # O(n^2) O(i*j)
        
point = (1, 2)

student = {
    'name': 'John',
    'age': 20,
}

numbers = {1, 2, 3, 4, 5}

if 3 in numbers:  # O(1)
    print('Found')