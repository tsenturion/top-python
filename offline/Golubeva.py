print("Задание 1 Пользователь вводит склавиатуры строку.Проверьте является ли введенная строка палиндромом. Палин слева направо и справа налево. Например, кок; А роза упала на лапу Азора; доход; А буду я у дуба.")
str = input("Введите строку")
if str == str[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")


print("Задание 2 Пользователь вводит склавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на экран измененный текст.")
text = input("Введите текст")
words = input("Введите список зарезервированых слов").split()
for word in words:
text = text.replace(word, word.upper())
print(text1)



print("Задание 3 Есть некоторый текст. Посчитайте в этом тексте количество предложенийивыведитенаэкранполученный результат")
txt = 'Кошке достаточно всего 1 секунды, чтобы перейти в бодрое состояние из глубоко сна. Даже во сне она продолжает ощущать запахи, звуки, различать речь и мгновенно отзывается на свою кличку.'
sentenxes = 0
for char in text:
    if char in ".!?":
        sentenxes +1
        print(sentenxes)

print("Задание 1 Пользователь вводит с клавиатуры число в диапазоне от 1 до 100. Если число кратно 3 (делится на 3 безостатка) нужно вывести слово Fizz. Если число кратно 5 нужновывестисловоBuzz.Если число кратно 3и5нужно вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число. Еслипользователь ввел значение не вдиапазонеот1 до 100 требуется вывести сообщение об ошибке.")

number = int(input("Введите число от 1 до 100: "))
if number < 1 or number > 100:
    print("Ошибка: число должно быть в диапазоне от 1 до 100.")
else:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

