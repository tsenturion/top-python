     #Задание 1
'''string_to_check = input("Введите строку для проверки: ")
cleaned_string = "".join(filter(str.isalnum, string_to_check.lower()))# Это строка выполняет очистку и приведение к нижнему регистру
if cleaned_string == cleaned_string[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")'''
    # Задание 2
'''translation = input('Введите предложение для перевода: ')
upper_translation = translation.upper()
print(upper_translation)'''
    # Задание 3
'''import re

sentences = input('Введите текст: ')
split_sentences = re.split(r'[.!?]+', sentences)# разбивает текст на части.
count = 0 # счет предложения на 0
for sentence in split_sentences:
  if sentence.strip():
    count +=1
print(f'Количество предложений: {count}')'''
# Задание 4
keyboard_input = input('Введите число от 1 до 100: ')
try:
    number = int(keyboard_input):
if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else: print(number)


