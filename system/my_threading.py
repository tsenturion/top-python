"""
threading
для чего нужны:
параллелизм
реактивность
эффектовное исполнение ожиданий 
маштабирование на многопроцессорных системах
I/O-bound задач

GIL

неэффективны:
многочисленные вычисления на CPU (тут нужен multiprocessing)

используем когда:
клиент-серверное взаимодействие
асинхронная запись логов
обработка пользовательского ввода 
таймеры и отложенные задачи
подкачка данных в фоне

race condition условная гонка/состояние гонки
deadlock взаимные блокировки
starvation голодание
трудность отладки

синхронизация потоков:
Lock - примитив синхронизации для управления доступом к общим ресурсам
Rlock, Semaphore, Condition, Event - для координации работы потоков
queue.Queue - потокобезная очередь для обмена данными между потоками
    put(item, block=True, timeout=None) - добавить элемент в очередь
    get(block=True, timeout=None) - получить элемент из очереди
    task_done() - сообщает очереди, что текущая задача выполнена
    join() - ожидание завершения всех потоков
    empty(), full(), qsize() - информация об очереди. Небезопасны

Thread - класс, реализующий поток исполнения кода
    передать целевую функцию через параметр target=
    создать свой класс на основе класса Thread и переопределить метод .run()

    .start() запуск потока
    .run() метод исполнения (для собственных классов)
    .join(timeout=None) - ожидание завершения потока, если не передан таймаут, то будет ждать пока не завершится поток
    .is_alive() - проверка на активность потока
    .name, .ident - имя и идентификатор потока

    жизненный цикл потока:
        Создан = Thread()
        Запущен = .start()
        Работает = .run()
        Завершен 

from concurrent.futures import ThreadPoolExecutor
    ThreadPool - многопоточная очередь задач

    Future
    future.done() - проверяет завершена ли задача
    future.result() - возвращает результат выполнения задачи
    future.exception() - возвращает исключение, если оно было
    future.add_done_callback(fn) - добавить функцию, которая будет вызвана после завершения задачи

Barrier - синхронизация потоков, когда все потоки должны дождаться друг друга
    wait(timeout=None) - ожидание завершения всех потоков
    BrokenBarrierError - исключение, когда все потоки не успели дождаться друг друга

Lock
    lock.acquire(blocking=True, timeout=-1) - захватить блокировку, если она свободна
    lock.release() - освободить блокировку
with lock:
    # код, который нужно защитить

RLock - рекурсивный замок

Semaphore(value) - для нескольких потоков можно использовать семафоры, 
    которые ограничивают количество одновременно выполняющихся потоков

    acquire(blocking=True, timeout=None) - попытка захватить семафор, уменьшая счетчик внутреннего состояния
    release() - освобождение семафора, увеличивая счетчик

    with semaphore:

    используем когда:
    ограничение количества подключений
    ограниение доступа к оборудования
    регулировка скорости работы 
    ограниченный пул

BoundedSemaphore() - счетчик должен быть больше нуля

Event - сигнализация между потоками
    .wait(timeout=None) - ожидание сигнала. Блокируется поток до тех пор, пока сигнал не будет установлен
    .set() - установка сигнала. Разблокирует все ожидающие потоки
    .clear() - сброс сигнала. Потоки снова будут заблокированы
    .is_set() - проверка состояния сигнала

Condition - расширенный механизм ожидания для оповещения других потоков, что событие произошло
    wait() - ожидание сигнала. Блокируется поток до тех пор, пока сигнал не будет установлен
    notify() / notify_all() - уведомление ожидающих потоков

    когда используем:
    производитель-потребитель
    ожидание готовности ресурса
    сигнал окончания работы

Timer - запуск потока через заданный интервал времени (Thread)
    t = Timer(interval, function, args=None, kwargs=None)
    interval - время задержки в секундах
    function - функция, которую нужно запустить
    args - аргументы для функции список
    kwargs - аргументы для функции словарь

    t.start()
    t.cancel()

    не используем когда:
    высокоточная задержка
    строгое управление временем повторяющихся событий 

    используем когда:
    один раз вызврать с задержкой
    отложить выполнение действия 
    прервать выполнение по истечению времени
    простой планировщик событий 

threading.current_thread() - возвращает текущий поток (объект)
threading.enumerate() - список всех активных потоков
threading.active_count() - количество активных потоков
threading.current_thread().name - имя потока
"""
from threading import Thread, current_thread, active_count, enumerate
import threading

def worker():
    print('работает поток', current_thread().name)

t = Thread(target=worker)
t.start()


class MyThread(Thread):
    def run(self):
        print("Работает поток через наследование")

t = MyThread()
t.start()


t = Thread(target=lambda: print('просто функция'))
t.start()
t.join()
print("все потоки завершили работу")


def greet(name, greeting='hello'):
    print(f'{greeting}, {name}')

t = Thread(target=greet, args=('Alice', ), kwargs={'greeting': 'Hi'})
t.start()


import time

def slow_task(name):
    print(f'Начал выполнение задачи {name}')
    time.sleep(0.1)
    print(f'Завершил выполнение задачи {name}')

threads = []
for i in range(3):
    t = Thread(target=slow_task, args=(f'task-{i}', ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('Все потоки завершили работу')


"""
создать список заказов (числа от 1 до 10)
для каждого заказа создать поток, который:
    - выводит сообщение
    - показывает имя потока

после запуска всех потоков
    - вывести количество активных потоков
    - вывести список всех активных потоков

дождаться завершения всех потоков
снова показать количество активных потоков
"""
def process_order(order_id):
    current = current_thread()
    print(f'[{current.name}] Начал обработку заказа {order_id}')
    time.sleep(0.1)
    print(f'[{current.name}] Завершил обработку заказа {order_id}')

def show_info():
    print(f"Количество активных потоков: {active_count()}")
    print('список активных потоков')
    for t in threading.enumerate():
        print(f'{t.name} - {t.ident}')

def main():
    orders = list(range(1, 11))

    threads = []
    for order_id in orders:
        t = Thread(target=process_order, args=(order_id, ))
        threads.append(t)
        t.start()

    show_info()

    for t in threads:
        t.join()

    show_info()


from threading import Lock

counter = 0
lock = Lock()

def increment():
    global counter
    for _ in range(1000000):
        with lock:
            global counter
            counter += 1

threads = [Thread(target=increment) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f'counter = {counter}')

"""if lock.acquire(timeout=1.5):
    try:
        # критическая секция
    finally:
        lock.release()
else:
    print('не удалось захватить ресурс')"""

from threading import RLock
lock = RLock()

def recursive(n):
    if n <= 0:
        return

    with lock:
        print(f'захват на глубине {n}')
        recursive(n - 1)

recursive(3)

lock1 = Lock()
lock2 = Lock()

"""
deadlock
def thread1():
    with lock1:
        print('захват lock1')
        time.sleep(1)
        print('пытаемся захватить lock2')
        with lock2:
            print('захватил lock2')

def thread2():
    with lock2:
        print('захват lock2')
        time.sleep(1)
        print('пытаемся захватить lock1')
        with lock1:
            print('захватил lock1')

t = Thread(target=thread1)
t.start()

t2 = Thread(target=thread2)
t2.start()"""

from threading import Semaphore
sema = Semaphore(2)

def worker(num):
    print(f"поток {num} ждет доступ ")
    with sema:
        print(f"поток {num} получил доступ")
        time.sleep(2)
        print(f"поток {num} освободил доступ")

threads = [Thread(target=worker, args=(i, )) for i in range(5)]

[t.start() for t in threads]
[t.join() for t in threads]

from threading import BoundedSemaphore
"""
sema = BoundedSemaphore(2)
sema.acquire()
sema.release()
sema.release()"""

import random

download_sema = Semaphore(3)

def download_file(file_id):
    print(f"Файл {file_id}: ожидание слота")
    with download_sema:
        print(f"Файл {file_id}: скачивается")
        time.sleep(random.randint(1, 3))
        print(f"Файл {file_id}: скачался")

threads = [Thread(target=download_file, args=(i, )) for i in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

"""
1 параллельная печать с блокировкой
5 потоков, печатают от 1 до 3. Поток в критичческой секции, защищен Lock
"""
lock = Lock()
def print_numbers(name):
    for i in range(1, 4):
        with lock:
            print(f"поток {name}: {i}")
        time.sleep(0.2)

threads = []

for i in range(5):
    t = Thread(target=print_numbers, args=(f"поток-{i}", ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

"""
2 рекурсивная блокировка
поток, вызывает функцию внутри функции (рекурсивный вызов). обе используют одну и ту же блокировку
"""
rlock = RLock()

def inner():
    with rlock:
        print('внутренняя функция')

def outer():
    with rlock:
        print('внешняя функция')
        inner()

t = Thread(target=outer)
t.start()
t.join()
"""
3 ограничение количества одновременных подключений
запустите 10 потоков, работают по 2 секу. Не более 3 потоков одновременно
"""
sem = Semaphore(3)
def worker(n):
    with sem:
        print(f"поток {n} захватил ресурс")
        time.sleep(2)
        print(f"поток {n} освободил ресурс")

threads = []
for i in range(10):
    t = Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

[t.join() for t in threads]

"""
4 контроль использования ресурса
создать BoundedSemaphore(2), попробовать вызвать release() больше чем acquire() раз. Обработка ошибок
"""
sem = BoundedSemaphore(2)

sem.acquire()
sem.acquire()
try:
    sem.release()
    sem.release()
    sem.release()
except ValueError as e:
    print(f'ошибка {e}')

"""
5 сравнение Lock и Semaphore
сделать принтер. использовать с lock, semaphore3
"""
printer_lock = Lock()
printer_sem = Semaphore(3)

def lock_user(n):
    with printer_lock:
        print(f"[Lock] Поток {n} использует принтер")
        time.sleep(1)

def sem_user(n):
    with printer_sem:
        print(f"[Semaphore] Поток {n} использует принтер")
        time.sleep(1)

print('Запуск потоков с Lock')
threads = [Thread(target=lock_user, args=(i, )) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print('Запуск потоков с Semaphore')
threads = [Thread(target=sem_user, args=(i, )) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()


"""
работа с общим складом
ограниченное количество ресурсов 5 едениц
поток = сотрудник, пытается взять ресурс, поработать с ним и вернуть его обратно
нужна синхронизация
lock Для количества выполненных операция
rlock Для функции, которая вызывает внутри себя другую функцию и обе их используют одну и ту же блокировку
semaphore Ограничить число потоков
bounded semaphore поменять на 
thread
вывести сообщение с именем потока и номером операции
взять ресурс, подождать
вернуть ресурс, обновить общий счетчик
"""
from threading import Lock, Thread, BoundedSemaphore, Semaphore, RLock
import threading
import random
import time

total_operations = 0
total_operations_lock = Lock()

rlock = RLock()
semaphore = Semaphore(3)
bounded_semaphore = BoundedSemaphore(5)

def update_operations():
    global total_operations
    with total_operations_lock:
        total_operations += 1


def nested_function():
    with rlock:
        print(f"[{threading.current_thread().name}] Внутренняя функция с RLock")

def function_with_rlock():
    with rlock:
        print(f"[{threading.current_thread().name}] Внешняя функция с RLock")
        nested_function()

def worker(employee_id):
    with semaphore:
        print(f"[{threading.current_thread().name}] Сотрудник {employee_id} ждет ресурс...")
        with bounded_semaphore:
            print(f"[{threading.current_thread().name}] Сотрудник {employee_id} получил ресурс")
            time.sleep(random.uniform(0.5, 1.5))
            update_operations()
            function_with_rlock()
            print(f"[{threading.current_thread().name}] Сотрудник {employee_id} вернул ресурс")

def main():
    threads = []
    for i in range(1, 11):
        t = Thread(target=worker, args=(i,), name=f"Сотрудник-{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Общее количество операций: {total_operations}")
    print(f"Количество активных потоков: {threading.active_count()}")
    print("Список активных потоков:", [t.name for t in threading.enumerate()])


from threading import Condition

condition = Condition

with condition:
    condition.wait()

with condition:
    condition.notify()
    
#while not data_ready: 
#    condition.wait()

"""
производитель-потребитель
общий список buffer, хранит максимум 5 элементов
производитель добавляет в список числа от 1 до 20
    если буфер заполнен, производитель ждет
    после добавления числа производитель уведомляет потребителя

потребитель извлекает элементы из буфера
    если буфер пуст, потребитель ждет до тех пор, пока не появится новый элемент (производитель добавляет)
    после извлечения элемента потребитель уведомляет производителя

threading.current_thread().name для отладки
"""
from threading import Thread, Condition
import threading
import time
import random

buffer = []
MAX_SIZE = 5

condition = Condition()

def producer():
    for i in range(1, 21):
        with condition:
            while len(buffer) == MAX_SIZE:
                print(f"Производитель [{threading.current_thread().name}] ожидает")
                condition.wait()

            buffer.append(i)
            print(f"Производитель [{threading.current_thread().name}] добавил элемент {i} в {buffer}")
            condition.notify()

        time.sleep(random.uniform(0.2, 0.6))

def consumer():
    for _ in range(20):
        with condition:
            while not buffer:
                print(f"Потребитель [{threading.current_thread().name}] ожидает")
                condition.wait()

            item = buffer.pop(0)
            print(f"Потребитель [{threading.current_thread().name}] извлек из {buffer} элемент {item}")
            condition.notify()

        time.sleep(random.uniform(0.3, 0.7))

def main():
    t1 = Thread(target=producer, name="Producer")
    t2 = Thread(target=consumer, name="Consumer")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Все потоки завершили работу")



from threading import Event
event = Event()
event.set()
event.clear()
if event.is_set():
    print("можно продолжить")
event.wait(timeout=None)


event = Event()

def worker():
    print("поток ожидает события")
    event.wait()
    print("поток получил событие")

t = Thread(target=worker)
t.start

time.sleep(2)
print("посылаю сигнал")
event.set()

t.join()


event = Event()

def ready_worker(i):
    print(f"поток {i} ждет запуска")
    event.wait()
    print(f"поток {i} стартует")

threads = [Thread(target=ready_worker, args=(i, )) for i in range(5)]
for t in threads: t.start()

time.sleep(2)
print("стартуем все потоки")
event.set()

#if not event.wait(timeout=1):
#    print("сигнала не было")

#event.set()
#thread.start()
from queue import Queue
q = Queue()
q = Queue(maxsize=10) # ограничение на кол-во элементов в очереди


def producer(q):
    for i in range(5):
        print("производитель отправляет данные")
        q.put(i)
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        print(f"получено: {item}")
        q.task_done()

q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()
t1.join()
q.join()

q = Queue(maxsize=3)

def producer():
    for i in range(5):
        print("производитель отправляет данные")
        q.put(i)
        print(f"{i} отправлен")

def consumer():
    while True:
        item = q.get()
        print(f"получено: {item}")
        time.sleep(2)
        q.task_done()

Thread(target=producer).start()
Thread(target=consumer, deamon=True).start()

q = Queue()

def producer():
    for i in range(5):
        q.put(f"data {i}")

def consumer():
    while True:
        item = q.get()
        print(f"получено: {item}")
        q.task_done()

for _ in range(2):
    Thread(target=consumer).start()

for _ in range(3):
    Thread(target=producer, deamon=True).start()


"""
t = Timer(interval, function, args=None, kwargs=None)
interval - время задержки в секундах
function - функция, которую нужно запустить
args - аргументы для функции список
kwargs - аргументы для функции словарь

t.start()
t.cancel()
"""

from threading import Timer

def say_hello():
    print('таймер сработал')

t = Timer(3, say_hello)
t.start()


def print_msg(msg):
    print(f"[{time.strftime('%X')}] {msg}")

print(f"[{time.strftime('%X')}] старт")
t = Timer(3, print_msg, args=("сообщение через 3 секунды",))
t.start()
print(f"[{time.strftime('%X')}] основной поток работает дальше")


def repeat():
    print(f"сейчас {time.strftime('%X')}")
    t = Timer(2, repeat)
    t.start()

repeat()


def timeout():
    print("время вышло")

t = Timer(2, timeout)
t.start()

anwer = input("введите ответ за 2 с: ")
t.cancel()
print(f"ответ: {answer}")


counter = 0
lock = Lock()

def increase():
    global counter
    with lock:
        counter += 1
        print(f"счетчик: {counter}")

t = Timer(2, increase)
t.start()
t.join()


"""
напоминалка
список напоминаний, в каждом
    сообщение - строка
    задержка в секундах
для каждого напоминания создать Timer, который через указанное время выводит сообщение

сразу запустить все таймеры
дождаться завершения

reminders = [
    ("сообщение 1", 1),
    ("сообщение 2", 2),
    ("сообщение 3", 3),
]
"""

def reminder(message, delay):
    print(f"[{threading.current_thread().name}] Напоминание: {message}")

def main():
    reminders = [
        ("сообщение 1", 1),
        ("сообщение 2", 2),
        ("сообщение 3", 3),
    ]
    
    timers = []

    for message, delay in reminders:
        t = Timer(delay, reminder, args=(message, delay))
        timers.append(t)
        t.start()
        print(f"[{threading.current_thread().name}] Напоминание создано: {message}, срабатывает через {delay} секунд")

    for t in timers:
        t.join()

    print(f"[{threading.current_thread().name}] Все напоминания завершены")


from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=5)

# 1 submit(fn, *args, **kwargs) - отправить задачу на выполнение
future = executor.submit(my_func, arg1, arg2)

result = future.result()
"""
Future
future.done() - проверяет завершена ли задача
future.result() - возвращает результат выполнения задачи
future.exception() - возвращает исключение, если оно было
future.add_done_callback(fn) - добавить функцию, которая будет вызвана после завершения задачи
"""
# 2 map(fn, *iterables) - выполнить функцию на нескольких элементах

results = executor.map(my_func, list_of_args)


def task(n):
    time.sleep(1)
    return n * 2

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

# без with 
# executor.shutdown(wait=True)
 
for r in results:
    print(r)


futures = []

for i in range(10):
    futures.append(executor.submit(my_func, i))

for f in futures:
    print(f.result())


def download(url):
    print(f"Скачиваем {url}")
    resp = requests.get(url)
    return len(resp.content)

urls = [
    "https://www.python.org",
    "https://www.google.com",
    "https://www.yandex.ru"
]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download, urls)

for size in results:
    print(f"размер ответа: {size}")


def worker(q):
    while not q.empty():
        item = q.get()
        print(f"получено: {item}")
        q.task_done()

q = Queue()
for i in range(20):
    q.put(i)

with ThreadPoolExecutor(max_workers=4) as executor:
    for _ in range(4):
        executor.submit(worker, q)


from threading import Barrier

barrier = Barrier(parties=3, timeout=3)
# barrier.broken
def worker():
    print("До барьера")
    barrier.wait()
    print("После барьера")

def worker():
    for phase in range(5):
        print(f"Поток {threadid.current_thread().name} в фазе {phase}")
        barrier.wait()

i = barrier.wait(timeout=3)
if i == 0:
    print("я последний и главный поток, начинаю финальную фазу")


barrier = Barrier(parties=3, timeout=3)

def worker(n):
    print(f"Поток {n} работа до барьера")
    time.sleep(n)
    print(f"Поток {n} подошел к барьеру")
    barrier.wait()
    print(f"Поток {n} продолжил выполнение")

threads = []

for i in range(3):
    t = Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

"""
есть производитель , который кладёт задачи (строки) в очередь
есть несколько потребителей, которые берут задачи из очереди и обрабатывают их
производитель должен положить в очередь ограниченное количество задач. например, 10
после завершения добавления задач производитель кладёт в очередь специальные маркеры завершения, чтобы сигнализировать потребителям о конце работы
потребители должны завершить работу после получения маркера None
"""

def producer(task_queue: Queue, num_tasks: int, num_consumers: int):
    for i in range(num_tasks):
        task = f"Task {i + 1}"
        print(f"[Producer] Produced task: {task}")
        task_queue.put(task)
        time.sleep(random.uniform(0.5, 1.5))

    for _ in range(num_consumers):
        task_queue.put(None)
    print("[Producer] Producer finished.")

def consumer(task_queue: Queue):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"[{threading.current_thread().name}] Consumer finished.")
            task_queue.task_done()
            break

        print(f"[{threading.current_thread().name}] Consumed task: {task}")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[{threading.current_thread().name}] Finished task: {task}")
        task_queue.task_done()

def main():
    num_tasks = 10
    num_consumers = 3
    task_queue = Queue()

    prod_thread = Thread(target=producer, args=(task_queue, num_tasks, num_consumers))

    cons_threads = [
        Thread(target=consumer, args=(task_queue,), name=f"Consumer {i + 1}")
        for i in range(num_consumers)
    ]

    prod_thread.start()
    for t in cons_threads:
        t.start()

    task_queue.join()

    prod_thread.join()
    for t in cons_threads:
        t.join()

    print("[Main] All tasks completed.")

"""
from queue import Queue
многопоточная обработка заданий из очереди 
producer - добавляет элементы в очередь
    task-1
    task-2
    task-N

несколько consumers - берут элементы из очереди и обрабатывают time.sleep(1)
основной поток ждет
завершение по сигналу (None/STOP)
"""

NUM_TASKS = 10
NUM_CONSUMERS = 3

task_queue = Queue()

def producer():
    for i in range(NUM_TASKS):
        task_name = f"task-{i}"
        print(f"[Producer] добавляем задачу {task_name}")
        task_queue.put(task_name)
        time.sleep(0.1)
    
    for _ in range(NUM_CONSUMERS):
        task_queue.put(None)

def consumer(thread_id):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"[Consumer {thread_id}] получили сигнал о завершении")
            task_queue.task_done()
            break
        print(f"[Consumer {thread_id}] обработка задачи {task}")
        time.sleep(0.5)
        print(f"[Consumer {thread_id}] задача {task} завершена")
        task_queue.task_done()

producer_thread = Thread(target=producer)
producer_thread.start()

consumer_threads = []
for i in range(NUM_CONSUMERS):
    t = Thread(target=consumer, args=(i,))
    t.start()
    consumer_threads.append(t)

task_queue.join()
producer_thread.join()
for t in consumer_threads:
    t.join()

print("Все задачи обработаны")

"""
ThreadPoolExecutor
многопоточная обработка веб запросов
submit
map
as_completed

многопоточная система обработки задач имитирующих загрузку с разных сайтов. Эмуляция через time.sleep() и случайный результат
10 запросов
обработка с помощью полу из 3-5 потоков
случайная задержка в обработке
возвращать результат и печатать его после завершения
обработка ошибок
"""

from concurrent.futures import as_completed

def fetch(url):
    delay = random.uniform(0.5, 2.0)
    print(f"[Start] Загрузка {url} с задержкой {delay:.2f} секунд")
    time.sleep(delay)

    if random.random() < 0.2:
        raise Exception(f"Ошибка загрузки {url}")

    print(f"[End] Загрузка {url} завершена")
    return f"Результат загрузки {url}"

urls = [f"http://site{i}.com" for i in range(1, 11)]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch, url): url for url in urls}

    for future in as_completed(futures):
        url = futures[future]
        try:
            result = future.result()
            print(f"Результат загрузки {url}: {result}")
        except Exception as exc:
            print(f"Ошибка загрузки {url}: {exc}")

"""
Barrier
синхронизация фаз работы потоков
три фазы
подготовка
выполнение
завершение

5 потоков
3 этапа с принтом
ожидание
случайная задержка
показать что синхронно начали следующую
"""

NUM_THREADS = 5

barrier = Barrier(NUM_THREADS)

def worker(thread_id):
    for phase in range(1, 4):
        time.sleep(random.uniform(0.5, 2.0))
        print(f"[Поток {thread_id}] завершил фазу {phase}, ждет")

        barrier.wait()

        if phase < 3:
            print(f"[Поток {thread_id}] переходит к фазе {phase + 1}")

threads = []
for i in range(NUM_THREADS):
    t = Thread(target=worker, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Все потоки завершили работу")