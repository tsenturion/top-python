"""
asyncio - асинхронный цикл событий. Для ввода/вывода, с ожиданием

event loop цикл событий
    ищет задачи для выполнения
    запускает задачу до ближайшего await
    переключается на следующую задачу
    возвращается к приостановленной задаче, когда данные готовы

корутины coroutine - функции
    async def - корутина
    await - ожидание

create_task - создает задачу и регистрирует ее в цикле событий

gather - запускает задачи и ожидает их завершения
    return_exceptions=True - возвращает исключения

wait - ожидает завершения задач
    return_when=ALL_COMPLETED - все задачи завершены
    return_when=FIRST_COMPLETED - первая задача завершена
    return_when=FIRST_EXCEPTION - первая задача завершена с ошибкой

cancel - отменяет задачу
    asyncio.CancelledError

asyncio.shield - защита от отмены

asyncio.Queue - очередь задач
    await queue.put(item) - добавить в очередь
    item = await queue.get() - получить из очереди
    queue.qsize() - размер очереди
    queue.task_done() - задача выполнена
    await queue.join() - ожидает завершения всех задач

    queue.empty() - очередь пуста queue.full() - очередь полна - не используем

asyncio.Lock - блокировка

asyncio.Semaphore - семафор
asyncio.BoundedSemaphore - ограниченный семафор

asyncio.Condition - условие

asyncio.Event - событие
asyncio.Barrier - барьер

LifoQueue - стек
PriorityQueue - очередь с приоритетами
"""
import asyncio
async def hello():
    print("hello")
    await asyncio.sleep(1)
    print('пока')

"""coro = hello()
asyncio.run(hello())"""

async def main():
    await some_coroutine()

#asyncio.run(main())
"""
ручное создание
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())

asyncio.create_task(my_coroutine())

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

loop.call_later(3, print, "прошло 3 секунды")
task = asyncio.create_task(some_coroutine())
task.cancel()
"""

async def say_hello():
    print('привет')

#coro = say_hello()

async def hello():
    print("привет")
    await asyncio.sleep(1)
    print('пока')

#asyncio.run(hello())

async def func1():
    print("func1 start")
    await asyncio.sleep(1)
    print("func1 end")

async def func2():
    print("func2 start")
    await func1()
    print("func2 end")


async def bad_task():
    while True:
        pass


async def fetch_data():
    await asyncio.sleep(1)
    return "some data"

async def process():
    data = await fetch_data()
    print(data)

#asyncio.run(process())

async def add(a, b):
    return a + b

async def main():
    result = await add(1, 2)
    print(result)

#asyncio.run(main())

#task = asyncio.create_task(my_coroutine())

async def job(n):
    await asyncio.sleep(1)
    print(f"готово: {n}")

async def main():
    tasks = [asyncio.create_task(job(n)) for n in range(10)]
    await asyncio.gather(*tasks)

#asyncio.run(main())

async def risky():
    raise ValueError("ошибка")

async def main():
    try:
        await risky()
    except ValueError as e:
        print(e)

#asyncio.run(main())

"""
асинхронная система загрузки и обработки данных 
корутина-поставщик fetch_data. Имитация asyncio.sleep с разным времен
корутина-обработчик process_data получает реультат загрузки и обрабатывает его. Подсчет символом
все параллельно, с create_task
gather чтобы дождаться всех задач
"""
async def fetch_data(name):
    delay = random.uniform(0.5, 2)
    print(f"[FETCH] Загрузка {name} с задержкой {delay:.2f} секунд")
    await asyncio.sleep(delay)
    data = f"данные_{name}_{random.randint(1, 100)}"
    print(f"[FETCH] Загрузка {name} завершена: {data}")
    return data

async def process_data(data):
    print(f"[PROCESS] Обработка данных: {data}")
    await asyncio.sleep(random.uniform(0.5, 2))
    result = len(data)
    print(f"[PROCESS] Обработка данных завершена: {result} символов")
    return result

async def main():
    sources = ["source1", "source2", "source3"]
    tasks = [asyncio.create_task(fetch_data(source)) for source in sources]

    results = await asyncio.gather(*tasks)
    process_tasks = [asyncio.create_task(process_data(data)) for data in results]
    processed = await asyncio.gather(*process_tasks)

    print(f"Всего задач: {len(tasks)}")
    print(f"Общее количество символов: {sum(processed)}")

async def say_hello():
    print("hello")
    await asyncio.sleep(1)
    #raise Exception
    print("world")
    
async def main():
    task = asyncio.create_task(say_hello())
    print("корутина запущена")
    await task

#asyncio.run(main())


async def say(word, delay):
    await asyncio.sleep(delay)
    return word

async def main():
    results = await asyncio.gather(
        say("hello", 1),
        say("world", 2),
        say("asyncio", 3)
    )
    print(results)

#asyncio.run(main())


async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} завершен"

async def main():
    tasks = [asyncio.create_task(task(f"задача {i}", i)) for i in range(5)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for d in done:
        print(d.result())

#asyncio.run(main())


async def say_hello():
    print("hello")
    await asyncio.sleep(1)
    print("hello again")

async def say_bye():
    print("bye")
    await asyncio.sleep(1)
    print("bye again")

async def main():
    await asyncio.gather(say_hello(), say_bye())

#asyncio.run(main())


async def do_work(number):
    print(f"начало задачи {number}")
    await asyncio.sleep(2)
    print(f"Задача {number} завершена")

async def main():
    tasks = [asyncio.create_task(do_work(n)) for n in range(1, 4)]
    await asyncio.gather(*tasks)

#asyncio.run(main())


async def hello():
    print("привет")
    await asyncio.sleep(1)
    print("пока")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


async def task1():
    await asyncio.sleep(2)
    print("задача 1 завершена")

async def task2():
    await asyncio.sleep(1)
    print("задача 2 завершена")

async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    print("обе задачи запущены")

    await t1
    await t2

# asyncio.run(main())

async def do_work(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} завершена")
    return name

async def main():
    result1 = await do_work("задача 1", 2)
    result2 = await do_work("задача 2", 1)
    print(f"результаты: {result1}, {result2}")

#asyncio.run(main())

async def main():
    task1 = asyncio.create_task(do_work("задача 1", 2))
    task2 = asyncio.create_task(do_work("задача 2", 1))
    print("задачи запущены")
    result1 = await task1
    result2 = await task2
    print(f"результаты: {result1}, {result2}")

#asyncio.run(main())

async def main():
    results = await asyncio.gather(
        do_work("задача 1", 2),
        do_work("задача 2", 1),
    )
    print(results)

#asyncio.run(main())

async def main_sequential():
    print("последовательное выполенение:")
    await do_work("задача 1", 2)
    await do_work("задача 2", 1)

async def main_with_tasks():
    print("запуск задач вручную:")
    task1 = asyncio.create_task(do_work("задача 1", 2))
    task2 = asyncio.create_task(do_work("задача 2", 1))
    await task1
    await task2

async def main_with_gather():
    print("запуск задач с gather:")
    await asyncio.gather(
        do_work("задача 1", 2),
        do_work("задача 2", 1),
    )

"""asyncio.run(main_sequential())
asyncio.run(main_with_tasks())
asyncio.run(main_with_gather())"""

async def main():
    await main_sequential()
    await main_with_tasks()
    await main_with_gather()
    
asyncio.run(main())


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

async def do_work(n):
    await asyncio.sleep(n)
    return f"задача {n} завершена"

async def main():
    tasks = [asyncio.create_task(do_work(n)) for n in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print(results)


#asyncio.run(main())

async def bad():
    raise ValueError("ошибка")

async def main():
    try:
        await asyncio.gather(hello(), say_hello(), return_exceptions=True)
    except ValueError as e:
        print(e)

#asyncio.run(main())

async def first():
    await asyncio.sleep(1)
    print("first")

async def second():
    await asyncio.sleep(3)
    print("second")

async def main():
    tasks = [asyncio.create_task(first()), asyncio.create_task(second())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()

    for task in done:
        print("завершена задача", task.result())


#asyncio.run(main())


"""
список серверов - асинхронные функции. ждет случайное время
некоторые падают с ошибкой

запустить опрос всех серверов одновременно
собрать все успешные ответы
обработать ошибки
показать время выполения
"""

import time
import random

async def ping_server(name: str) -> str:
    delay = random.uniform(0.5, 2)
    await asyncio.sleep(delay)
    if random.randint(1, 4) == 1:
        raise Exception(f"ошибка сервера {name}")
    return f"ответ сервера {name} получен"


async def main():
    servers = ["server1", "server2", "server3", "server4"]

    start = time.monotonic()

    tasks = [asyncio.create_task(ping_server(server)) for server in servers]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for name, result in zip(servers, results):
        if isinstance(result, Exception):
            print(f"ошибка сервера {name}: {result}")
        else:
            print(result)

    end = time.monotonic()
    print(f"время выполнения: {end - start:.2f} секунд")


#asyncio.run(main())

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"продукт {i} добавлен в очередь")
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"продукт {item} получен из очереди")
        queue.task_done()

queue = asyncio.Queue()

async def main():
    await asyncio.gather(
        producer(queue),
        consumer(queue),
        consumer(queue),
    )

#asyncio.run(main())

lock = asyncio.Lock()
counter = 0

async def increment():
    global counter
    async with lock:
        tmp = counter
        await asyncio.sleep(0.1)
        counter = tmp + 1


sem = asyncio.Semaphore(3)
async def limited_worker(id):
    async with sem:
        print(f"рабочий {id} начал работу")
        await asyncio.sleep(1)
        print(f"рабочий {id} закончил работу")

condition = asyncio.Condition()
items = []

async def producer():
    async with condition:
        items.append("item")
        condition.notify()

async def consumer():
    async with condition:
        await condition.wait()
        print("получено", items.pop())

event = asyncio.Event()
async def waiter():
    print("ожидание")
    await event.wait()
    print("продолжение")

async def trigger():
    await asyncio.sleep(1)
    event.set()

"""await asyncio.gather(waiter(), trigger())


queue = asyncio.PriorityQueue()
await queue.put((1, "низкий приоритет"))
await queue.put((0, "высокий приоритет"))

item = await queue.get()"""


"""
асинхронная система обработки заказов
производитель - потребитель
Queue
Lock
Event
gather
create_task
Class Order

кафе
Клиенты производители
Кухня потребитель
обработанные заказы в список готовых
клиенты ждут через Event

5 клиентов на кухню
"""

async def worker(name, delay):
    await asyncio.sleep(delay)
    print(f"Задача {name} завершилась")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("A", 2))
        tg.create_task(worker("B", 2))

asyncio.run(main())

        
