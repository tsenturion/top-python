
import asyncio
import random
import time

"""
Часть 1. Последовательное выполнение (await)
Напишите функцию async def do_work(name, delay), которая:
печатает сообщение о начале работы;
делает await asyncio.sleep(delay);
печатает сообщение о завершении;
возвращает имя задачи.
Напишите функцию async def sequential_demo(), которая вызывает do_work("A", 2) и do_work("B", 1) последовательно с помощью await.
Замерьте общее время выполнения этой функции (используйте time.perf_counter).

Вопрос:
Сколько времени заняла программа?
Почему выполнение заняло именно столько времени?
"""
async def do_work(name, delay):
    print(f"Начало работы с {name}")
    await asyncio.sleep(delay)
    print(f"Завершение работы с {name}")
    return name

async def sequential_demo():
    start = time.perf_counter()
    await do_work("A", 2)
    await do_work("B", 1)
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.2f} секунд")

#asyncio.run(sequential_demo())
"""
Часть 2. Запуск через create_task
Напишите функцию async def tasks_demo(), в которой:
создайте две задачи task1 и task2 через asyncio.create_task;
сразу после запуска выведите сообщение «Задачи запущены»;
дождитесь завершения обеих задач через await task1 и await task2.
Замерьте общее время выполнения.

Вопрос:
Чем отличается вывод программы от последовательного запуска?
Почему общее время меньше?
"""
async def tasks_demo():
    start = time.perf_counter()
    task1 = asyncio.create_task(do_work("A", 2))
    task2 = asyncio.create_task(do_work("B", 1))
    print("Задачи запущены")
    await task1
    await task2
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.2f} секунд")

#asyncio.run(tasks_demo())
"""
Часть 3. Использование asyncio.gather
Напишите функцию async def gather_demo(), которая запускает do_work("A", 2) и do_work("B", 1) с помощью asyncio.gather.
Замерьте время выполнения и сравните его с предыдущими частями.

Вопрос:

Чем gather отличается от ручного создания задач?
В каких случаях gather удобнее?
"""
async def gather_demo():
    start = time.perf_counter()
    await asyncio.gather(
        do_work("A", 2),
        do_work("B", 1)
    )
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.2f} секунд")

#asyncio.run(gather_demo())
"""
Часть 4. задание
Добавьте третью задачу do_work("C", 3).
Сравните выполнение при:
последовательном await,
ручном create_task,
использовании gather.
Постройте таблицу:

Метод	Общее время выполнения	Порядок завершения задач
await	
create_task
gather
"""
async def sequential_three():
    start = time.perf_counter()
    await do_work("A", 2)
    await do_work("B", 1)
    await do_work("C", 3)
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.2f} секунд")

async def tasks_three():
    start = time.perf_counter()
    t1 = asyncio.create_task(do_work("A", 2))
    t2 = asyncio.create_task(do_work("B", 1))
    t3 = asyncio.create_task(do_work("C", 3))
    print("Задачи запущены")
    await t1
    await t2
    await t3
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.2f} секунд")

async def gather_demo():
    start = time.perf_counter()
    await asyncio.gather(
        do_work("A", 2),
        do_work("B", 1),
        do_work("C", 3)
    )
    end = time.perf_counter()
    print(f"Время выполнения: {end - start:.2f} секунд")

async def main():
    await sequential_three()
    await tasks_three()
    await gather_demo()

asyncio.run(main())
"""
Часть 5. Вопросы
Почему await в последовательном варианте не дал конкурентности?
В чём разница между create_task и gather?
Почему asyncio.run обычно вызывается только один раз в программе?
Как вы объясните словами: «где именно происходит асинхронность»?
"""


