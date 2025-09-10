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
    queue.empty() - очередь пуста
    queue.full() - очередь полна
    queue.task_done() - задача выполнена

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

await asyncio.gather(waiter(), trigger())


queue = asyncio.PriorityQueue()
await queue.put((1, "низкий приоритет"))
await queue.put((0, "высокий приоритет"))

item = await queue.get()


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