#string = input("Введите строку: ")
string = "А роза упала на лапу Азора"
str = ''
for i in string:
    if i == ' ':
        continue
    else:
        str = str + i.lower()
if str == str[::-1]:
    print(f'"{string}" является палиндромом')
else:
    print(f'"{string}" не является палиндромом')

string = "А роза упала на лапу Азор"
str = ''
for i in string:
    if i == ' ':
        continue
    else:
        str = str + i.lower()
if str == str[::-1]:
    print(f'"{string}" является палиндромом')
else:
    print(f'"{string}" не является палиндромом')