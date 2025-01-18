"""
Задание 1
 Пользователь вводитсклавиатурыстроку.Проверьте
является ли введенная строка палиндромом. Палин
слева направо и справа налево. Например, кок; А роза
упала на лапу Азора; доход; А буду я у дуба.

 Задание 2
 Пользователь вводитсклавиатурынекоторыйтекст,
послечегопользовательвводитсписокзарезервированных
слов. Необходимонайтивтекстевсезарезервированные
слова и изменить их регистр на верхний. Вывести на
экран измененный текст.
Задание 3
 Есть некоторый текст. Посчитайте в этом тексте ко
личество предложенийивыведитенаэкранполученный
результат
-------------------------------------------------------------
Задание 1
 Пользователь вводит с клавиатуры число в диапа
зоне от 1 до 100. Если число кратно 3 (делится на 3 без
остатка) нужно вывести слово Fizz. Если число кратно 5
нужновывестисловоBuzz.Есличислократно3и5нужно
вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
вывести само число.
Еслипользователь ввел значение не вдиапазонеот1
до 100 требуется вывести сообщение об ошибке.
 Задание 2
 Написать программу, которая по выбору пользова
теля возводит введенное им число в степень от нулевой
до седьмой включительно.
 Задание 3
 Написать программу подсчета стоимости разговора
для разныхмобильныхоператоров.Пользовательвводит
стоимость разговора и выбирает с какого на какой опе
ратор он звонит. Вывести стоимость на экран
Задание 4
 Зарплатаменеджерасоставляет200$+процентотпро
даж, продажидо500$—3%,от500до1000—5%,свыше
1000 — 8%. Пользователь вводит с клавиатуры уровень
продаж для трех менеджеров. Определить их зарплату,
определить лучшего менеджера, начислить ему премию
200$, вывести итоги на экран
---------------------------------------------------------------------------
Задание 1
 Показать на экран все простые числа в диапазоне,
указанном пользователем. Число называется простым,
если оноделитсябезостаткатольконасебяинаединицу.
Например, три — это простое число, а четыре нет.
 Задание 2
 Показатьнаэкранетаблицуумножениядлявсехчисел
от 1 до 10. Например:
 1 * 1 = 1          1 * 2 = 2   …..  1 * 10  = 10
 .........................................................................
 10 * 1 = 10    10 * 2 = 20 …. 10 * 10 = 100.
 Задание 3
 Показать на экран таблицу умножения в диапазоне,
указанном пользователем. Например, если пользователь
указал 3 и 5, таблица может выглядеть так
 3*1 = 3    3*2 = 6       3*3 = 9       ...     3 * 10 = 30
.....................................................................................
 5*1 = 5    5 *2 = 10    5 *3 = 15    ...     5 * 10 = 50
"""
"""print('1234567890'.find('r', 5, 10)) # возвращает индекс первого вхожденич подстроки

someStr = '123z121saf253'
print(someStr)

new_str = someStr.replace('123', '2')
print(new_str)
length1 = len([1, 2, 3])
length2 = len(someStr)
list2 = ['123', '123']
sorted1 = sorted(someStr)
print(sorted1)
print(''.join(sorted1))
msg = ' 3 4 456  456456 6 5 '
print(msg.split())
print(msg.strip())
"""
""" Решение 1
def is_palindrome(text):
    processed_text = "".join(text.lower().split())
    return processed_text == processed_text[::-1]

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
"""
"""Решение 2
def modify_text(text, reserved_words):

    modified_text = text
    for word in reserved_words:
        modified_text = modified_text.replace(word, word.upper())
    return modified_text

text = input("Введите текст: ")

reserved_words_input = input("Введите зарезервированные слова через запятую: ")
reserved_words = [word.strip() for word in reserved_words_input.split(',')]

modified_text = modify_text(text, reserved_words)
print("Измененный текст:")
print(modified_text)
"""
"""Решение 3
import re

def count_sentences(text):

  sentence_endings = re.compile(r'[.!?]+')
  sentences = sentence_endings.findall(text)
  return len(sentences)

text = input("Введите текст: ")

sentence_count = count_sentences(text)
print("Количество предложений в тексте:", sentence_count)
"""

"""Решение 4
def fizz_buzz(number):

    if not 1 <= number <= 100:
       return "Ошибка: число должно быть в диапазоне от 1 до 100."
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

while True:
    try:
      user_input = int(input("Введите число от 1 до 100: "))
      break
    except ValueError:
       print("Ошибка: пожалуйста, введите целое число.")

result = fizz_buzz(user_input)
print(result)
"""
"""Решение 5
def power_calculator(number):

    print("Выберите степень (от 0 до 7):")
    while True:
      try:
        power = int(input())
        if 0 <= power <= 7:
             break
        else:
             print("Ошибка: введите число от 0 до 7.")
      except ValueError:
         print("Ошибка: введите целое число.")
    result = number ** power
    print(f"{number} в степени {power} = {result}")

while True:
    try:
        user_number = float(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка: введите число.")

power_calculator(user_number)
"""

"""Решение 6

def calculate_call_cost(duration, from_operator, to_operator):

    tariffs = {
        ("A", "A"): 0.5,
        ("A", "B"): 1.0,
        ("A", "C"): 1.2,
        ("B", "A"): 1.0,
        ("B", "B"): 0.6,
        ("B", "C"): 1.1,
        ("C", "A"): 1.2,
        ("C", "B"): 1.1,
        ("C", "C"): 0.7,
    }

    if (from_operator, to_operator) not in tariffs:
        return "Ошибка: Неизвестная комбинация операторов."

    cost_per_minute = tariffs[(from_operator, to_operator)]
    cost = duration * cost_per_minute
    return cost

while True:
  try:
     duration = float(input("Введите длительность разговора (в минутах): "))
     if duration >= 0:
        break
     else:
        print("Ошибка: длительность разговора не может быть отрицательной.")
  except ValueError:
      print("Ошибка: пожалуйста, введите число.")

while True:
   from_operator = input("Выберите оператора, с которого звонят (A, B, C): ").upper()
   if from_operator in ["A", "B", "C"]:
        break
   else:
        print("Ошибка: выберите оператора из списка A, B, C.")

while True:
    to_operator = input("Выберите оператора, на который звонят (A, B, C): ").upper()
    if to_operator in ["A", "B", "C"]:
         break
    else:
         print("Ошибка: выберите оператора из списка A, B, C.")


cost = calculate_call_cost(duration, from_operator, to_operator)

if isinstance(cost, str):
    print(cost)
else:
    print(f"Стоимость разговора: {cost:.2f} руб.")
"""

"""Решение 7

def calculate_salary(sales):

    base_salary = 200
    if sales <= 500:
        bonus_percentage = 0.03
    elif sales <= 1000:
        bonus_percentage = 0.05
    else:
        bonus_percentage = 0.08
    bonus = sales * bonus_percentage
    salary = base_salary + bonus
    return salary

def find_best_manager(sales_list):

    best_manager_index = 0
    best_sales = sales_list[0]
    for i, sales in enumerate(sales_list):
        if sales > best_sales:
           best_sales = sales
           best_manager_index = i
    return best_manager_index

sales_list = []
for i in range(3):
   while True:
      try:
         sales = float(input(f"Введите объем продаж для менеджера {i+1}: "))
         if sales >= 0:
            sales_list.append(sales)
            break
         else:
            print("Ошибка: уровень продаж не может быть отрицательным.")
      except ValueError:
           print("Ошибка: пожалуйста, введите число.")

salaries = [calculate_salary(sales) for sales in sales_list]

best_manager_index = find_best_manager(sales_list)

salaries[best_manager_index] += 200

print("\nИтоги:")
for i, salary in enumerate(salaries):
    print(f"Зарплата менеджера {i+1}: {salary:.2f}$")

print(f"\nЛучший менеджер: {best_manager_index+1}")
print(f"Зарплата лучшего менеджера с премией: {salaries[best_manager_index]:.2f}$")
"""

"""Решение 8

def is_prime(number):

    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_in_range(start, end):

    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
           primes.append(number)
    return primes

while True:
   try:
      start = int(input("Введите начало диапазона: "))
      end = int(input("Введите конец диапазона: "))
      if start >= 0 and end >= start:
         break
      else:
         print("Ошибка: начало диапазона не может быть отрицательным и не должно превышать конец диапазона")
   except ValueError:
       print("Ошибка: пожалуйста, введите целые числа.")

prime_numbers = find_primes_in_range(start, end)
print(f"Простые числа в диапазоне от {start} до {end}: {prime_numbers}")
"""
"""Решение 9

def print_multiplication_table():

  for i in range(1, 11):
    for j in range(1, 11):
      print(f"{i} * {j} = {i * j:<4}", end="  ")
    print()

print_multiplication_table()
"""

"""Решение 10

def print_multiplication_table_range(start, end):

    for i in range(start, end + 1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j:<4}", end="  ")
        print()

while True:
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
        if start >= 0 and end >= start:
            break
        else:
           print("Ошибка: начало диапазона не может быть отрицательным и не должно превышать конец диапазона")
    except ValueError:
        print("Ошибка: пожалуйста, введите целые числа.")

print_multiplication_table_range(start, end)
"""