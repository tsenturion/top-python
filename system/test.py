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

if __name__ == "__main__":
    main()