"""
time
timeit
datetime
platform

math
random

re
string

functools
"""

#pip install название модуля


"""import platform
import platform as pl
from platform import architecture
from platform import architecture as arch"""

"""from platform import *

print(architecture())  # архитектура
print(machine())  # тип машины
print(node())  # сетевое имя машины
print(platform())  # строка идентифицирующая базовую платформу
print(processor())  # имя процессора
print(system())  # имя ОС
print(release()) # версия ОС
print(version()) # доп информация об ОС
print(python_version()) # версия питона
print(python_build()) # информация о сборке python
print(python_compiler()) # о компиляторе

from time import *

print(time()) # колво сек с 1970
temp2 = time()
#print(sleep(1)) задержка в сек
print(localtime()) # колво сек с 1970 преобразуется в локальное время, объект struct_time
print(gmtime()) # колво сек с 1970 в utc, объект struct_time
temp = gmtime()
print(mktime(temp)) # объект struct_time в секунды"""

#шаблоны
"""
%Y: Год в формате четырех цифр
%m: Месяц в формате двух цифр (01-12)
%d: День месяца в формате двух цифр (01-31)
%H: Час в формате двух цифр (00-23)
%M: Минуты в формате двух цифр (00-59)
%S: Секунды в формате двух цифр (00-59)
%p: Префикс AM или PM для 12-часового формата
%I: Час в 12-часовом формате (01-12)
%Z: Имя часового пояса
%z: Смещение часового пояса в формате +HHMM или -HHMM
%A: День недели в полном формате
%B: Месяц в полном формате
%c: Строка даты и времени в стандартном формате
%x: Строка даты в стандартном формате
%X: Строка времени в стандартном формате
%j: Номер дня в году (001-366)
%U: Номер недели в году (00-53), начиная с воскресенья
%W: Номер недели в году (00-53), начиная с понедельника
%V: Номер недели в году (01-53), начиная с понедельника (ISO)
%G: Год в формате четырех цифр для номера недели ISO
%g: Год в формате двух цифр для номера недели ISO
%F: Дата в виде YYYY-MM-DD
%D: Дата в виде MM/DD/YY
%n: Символ перевода строки
%t: Символ табуляции
%r: Время в 12-часовом формате (час:минута:секунда AM/PM)
%R: Время в 24-часовом формате (час:минута)
%T: Время в 24-часовом формате (час:минута:секунда)
%s: Секунды с начала эпохи (Unix timestamp)
%a: Сокращенное название дня недели
%b: Сокращенное название месяца
%y: Год в формате двух цифр
%f: Микросекунды (000000-999999)
"""
#примеры только fms, s
"""
fmt = "%Y-%m-%d %H:%M:%S"
s = "2022-12-31 23:59:59"
"""


"""print(strftime(fmt, t)) # форматирует объект struct_time в строку на основе шаблона fmt
print(strptime(s, fmt)) # преобразует строку s в объект struct_time на основе шаблона fmt"""
"""print(ctime(temp2)) # преобразует секунды с начала эпохи в строку

print(perf_counter()) # высокоточное время с начала
print(monotonic()) # монотонное время (всегда увеличивается)

print(process_time()) # процессорное время, использованное текущим процессом
"""
# datetime

"""
классы:

date - дата (год, месяц, день)
    year, month, day - атрибуты для доступа
    today() - возвращает текущую дату
    fromtimestamp(timestamp) - преобразует метку времени в дату
    
time - время (час, минута, сек, микросекунда)
    hour, minute, second, microsecond - атрибуты
    
datetime - объединение
    year, month, day, hour, minute, second, microsecond - атрибуты
    now() - возвращает ткущую дату и время
    today() - текущую дату
    strptime(sting, format) - парсит строку в объект datetime
    strftime(format) - формирует объект datetime в строку
    combine(date, time) - объединяет 
    
timedelta - разница между двумя датами или временем
    days, seconds, microseconds - атрибуты
    
tzinfo, timezone - для часовых поясов

"""
from datetime import date, time, datetime as dt, timedelta as td

d = date(2025, 3, 17)
print(d)

today = date.today()
print(today)

t = time(21, 49, 34, 34)
print(t)

dt = dt(2025, 3, 17, 21, 59)
print(dt)

now = dt.now()
print(now)

formatted_dt = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_dt)

delta = td(days=7)

next_week = dt.now() + delta
print(next_week)

# timeit

from timeit import *
#timeit()
"""
stmt - код для замера
setup - перед замером
timer - таймер
number - кол-во раз выполнения
globals - пространство имен
"""
#Timer - класс
#.repeat() - метод выполнения измерения

code1 = """
result = 0
for i in range(10000):
    result += 1
"""
code2 = """
result = sum(range(10000))
"""
t1 = timeit(stmt=code1, number=100)
t2 = timeit(code2, number=100)
print(t1)
print(t2)

# import math
from random import *

#управление состоянием генератора
seed(42) # фиксация случайных
getstate() # возвращает текущее состояние генератора
setstate(state) # устанавливает состояние генератора

print(random()) # случайное 0.0-1.0
print(randint(a, b)) # случайное [a-b]
print(randrange(a, b, c)) #случайное из диапазона
print(uniform(a, b)) #слуаное дробное [ab]
print(choice(squence)) #случайный элемент из последовательности
print(shuffle(squence)) # перемешивает последовательность на месте
print(sample(population, k)) # population - последовательность, k уникальных элементов

