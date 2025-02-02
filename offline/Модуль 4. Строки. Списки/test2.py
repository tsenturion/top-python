strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
"""сделать первые буквы заглавными map, lambda"""

repl = lambda x: x.title()
for i in map(repl, strlist):
    print(i)

list2 = list(map(repl, strlist))
print(list2)
list2 = list(map(lambda x: x.title(), strlist))
print(list2)