"""
GIL

Process - отдельный процесс
Queue - очередь
Pipe - канал
Pool - для работы с группой процессов
Value, Array, Manager - механизмы для общего доступа к данным между процессами
"""

from multiprocessing import Process
import time

def say_hello():
    print()
    print("я работаю в отдельном процессе")
    time.sleep(1)
    print("конец")
    print()

def print_square(x):
    print("квадрат числа {0} равен {1}".format(x, x*x))

def show_info():
    from multiprocessing import current_process
    print("текущий процесс", current_process().name)
    print("идентификатор процесса", current_process().pid)

class MyProcess(Process):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        print(f"процесс получил {self.text}")

def worker(n):
    print(f"процесс {n} начал работу")
    time.sleep(5)
    print(f"процесс {n} закончил работу")

"""
создан (после p = Process(...))
запущен (после p.start())
ожидает завершения / ожидаемый (после p.join() - блокирует, пока не завершится)
завершен (после завршения функции)
"""


    
"""
запуск 5 процессов, работа через sleep
логирование

каждый процесс получает разное/случайное [1-5]c. время работы
использовать args
использовать join
"""
# from multiprocessing import Process
# import time

def sleeper(seconds, process_number):
    print(f"[{process_number}] Сон {seconds} секунд...")
    time.sleep(seconds)
    print(f"[{process_number}] Время проснулся!")

# if __name__ == '__main__':
#     delays = [3, 2, 4, 1, 5]
#     processes = []

#     for i, delay in enumerate(delays, start=1):
#         p = Process(target=sleeper, args=(delay, i))
#         processes.append(p)
#         print(f"[{i}] Процесс запущен!")
#         p.start()
    
#     for p in processes:
#         p.join()

#     print("Все процессы завершены!")
    
# 4 параллельных процесса. Каждый находит сумму квадратов в диапазоне
# from multiprocessing import Process
# import time

def sum_of_squares(start, end):
    print(f"процесс считает сумму квадратов от {start} до {end}")
    t1 = time.time()
    result = sum(x * x for x in range(start, end + 1))
    t2 = time.time()
    print(f"сумма квадратов от {start} до {end} равна {result} (время работы {t2 - t1} сек)")

if __name__ == '__main__':
    ranges = [
        (1, 250_000),
        (250_001, 500_000),
        (500_001, 750_000),
        (750_001, 1_000_000)
    ]

    processes = []

    start_time = time.time()

    for r in ranges:
        p = Process(target=sum_of_squares, args=r)
        processes.append(p)
        print("процесс запущен для диапазона", r)
        p.start()

    for p in processes:
        p.join()

    print("все процессы завершены")
    print("общее время работы", time.time() - start_time)

# добавить в задание 2. Задать каждому процессу имя и показать
# имя процесса
# pid
# is_alive()
# start_time, end_time