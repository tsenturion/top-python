"""
есть производитель , который кладёт задачи (строки) в очередь
есть несколько потребителей, которые берут задачи из очереди и обрабатывают их
производитель должен положить в очередь ограниченное количество задач. например, 10
после завершения добавления задач производитель кладёт в очередь специальные маркеры завершения, чтобы сигнализировать потребителям о конце работы
потребители должны завершить работу после получения маркера None
"""
from queue import Queue
from threading import Timer, Thread
import threading
import time
import random

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

if __name__ == "__main__":
    main()