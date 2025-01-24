#string = input("Введите строку: ")
from os.path import split

string = "сестра аня дядя петя брат паша мама тоня папа олег"
reserve_words = "аня петя паша тоня олег"

split_string = string.split()
split_reserve_words = reserve_words.split()
result_string = ''

for i in split_string:
    if i in split_reserve_words:
        result_string += i.capitalize() + ' '
    else:
        result_string += i + ' '
print(result_string)



