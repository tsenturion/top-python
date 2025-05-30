from gettext import textdomain
from pdb import runctx
from random import sample, choice, shuffle
from re import match
from string import *
from re import *
import re

print(ascii_letters)
print(ascii_lowercase)
print(ascii_uppercase)
print(digits)
print(hexdigits)
print(octdigits)
print(whitespace)
print(punctuation)

"""
создать паттерн для номеров телефона, такой, чтобы для
r''
Добавить:

начало
первые символов +7(
три случайных числа
)
три случайных числа
-
два случайных числа
-
два случайных числа
конец

pattern = r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$'

создать случайный логин и пароль
логин - заглавная буква + 10 строчных
пароль - заглавная, символ, 10 строчных"""

from random import *
login = choice(ascii_uppercase)
login += ''.join(choices(ascii_lowercase, k=10))
password = choice(ascii_uppercase)
password += ''.join(choice(punctuation))
password += ''.join(choices(ascii_lowercase, k=10))
print(login)
print(password)
a = randint(1, 10)
# перемешать сиволы в пароле
# random
# random() [0.0, 1.0) float случайное числе
# randint(1, 10) случайное int от а до б
# choise случайный элемент из последовательности
# sample список из k уникальных элементов из последовательности
# uniform() случайное с плавающей запятой от а до б
# randrange
# choises
# shuffle - перемешивает
"""password2 = password
password2 = list(password2)
shuffle(password2)"""

pattern = r'.' # один любой символ
print(bool(match(pattern, '..')))

pattern = r'^qwe' # начало строки
print(bool(match(pattern, 'qwe')))

pattern = r'qwe$' # конец строки
print(bool(match(pattern, 'qwe')))

pattern = r'\.*' # любые символы, много
print(bool(match(pattern, '.2334')))

pattern = r'ab+8' # любое количество определенных символов
print(bool(match(pattern, 'ab888')))

pattern = r'ab?8$' # один конкретный символ
print(bool(match(pattern, 'ab8')))

pattern = r'ab{5}' # заданное количество повторений до {
print(bool(match(pattern, 'abbbbb')))

pattern = r'[123]$' # вхождение любого одного из [внутри]
print(bool(match(pattern, '3')))

pattern = r'[^b]$' # кроме вхождение любого одного из [внутри]
print(bool(match(pattern, 'a')))

pattern = r'(12|32)(12|45)' # или
print(bool(match(pattern, '1232')))

pattern = r'\d' # число
print(bool(match(pattern, '1')))

pattern = r'\d{11}' # 11 цифр
print(bool(match(pattern, '81231231212')))

pattern = r'\d{11, }' # 11 цифр и более
print(bool(match(pattern, '81231231212')))

pattern = r'\d{11, 15}' # от 11 до 15
print(bool(match(pattern, '81231231212')))

pattern = r'\D' # не число
print(bool(match(pattern, '1')))

pattern = r'\w' # буква цифра подчеркивание
print(bool(match(pattern, '1')))

pattern = r'\W' # кроме буква цифра подчеркивание
print(bool(match(pattern, '1')))

pattern = r'\s' # whitespace
print(bool(match(pattern, '1')))

pattern = r'\S' # не whitespace
print(bool(match(pattern, '1')))

pattern = r'.*\bqwe\b.*' # граница слова
print(bool(match(pattern, '1 qwe 123')))

pattern = r'^.\Brty\B.$' # внутри слова
print(bool(match(pattern, 'qrtyq')))



pattern = r'\d{}' # 11 цифр
print(bool(match(pattern, "str")))

pattern = r'[a-zA-Z5-7]' # 11 цифр
print(bool(match(pattern, "str")))

str4 = 'qweqw@tu.riu'
str1 = '+7(123)123-23-23'
str2 = '+7(666)666-66-66'
str3 = '+7(66)666-66-66'
"""
создать паттерн для номеров телефона, такой, чтобы для
r''
Добавить:

начало
первые символов +7(
три случайных числа
)
три случайных числа
-
два случайных числа
-
два случайных числа
конец

str1 True
str2 True
str3 False
pattern = r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$'

"""
pattern = r'^\w+[\.\w-]*@\w+[\.\w-]*\.\w+[\.\w-]*$' # 11 цифр
print(bool(match(r'^\w+[.\w-]*@\w+[.\w-]*\.\w+[.\w-]*$', 'e....6...------@')))

"""
match(pattern, string, flags=0)
совпадаения в начале строки, Match если найдено, иначе None

"""
#совпадение в любом месте строки, Match если найдено, иначе None
#(pattern, string, flags=0)
match1 = search(r'\d+', '123qwe333')
print(match1.group())

#(pattern, string, flags=0)
#список всех совпадений шаблона в строке
matches = findall(r'\d+', '123qwe333')
print(matches)

#(pattern, string, flags=0)
#возвращает итератор с объектами Match для каждого совпадения
matches = finditer(r'\d+', '123qwe333')
for i in matches:
    print(i.group())

#(pattern, string, maxspit=0, flags=0)
#разделяет строку по шаблону и возвращает список частей
result = split(r'\s+', '123qwe333\tqweqwqw  qwe')
print(result)

#(pattern, repl, string, count=0, flags=0)
# заменяет все совпадения шаблона на указанную строку или результат функци
result = sub('\d+','', '123qwe333\tqweqwqw  qwe')
print(type(result).__name__) #str

#кортеж
result = subn('\d+','', '123qwe333\tqweqwqw  qwe')
print(type(result).__name__) #tuple

#(pattern, string, flags=0)
# соответствие всей строки шаблону
result = fullmatch(r'\d+', '12345')
print(bool(result))

#(pattern, flags=0)
#компилирует pattern в объект
pattern = compile('\d+')

#(string)
# делает экранирование
result = escape('1+1=2')
print(result)
match = search(pattern, 'gvugvugv123')
print(match.group())

# очистка
purge()