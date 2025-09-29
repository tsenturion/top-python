import asyncio
import aiohttp

async def worker(name, delay):
    await asyncio.sleep(delay)
    print(f"Задача {name} завершилась")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker("A", 2))
        tg.create_task(worker("B", 2))

#asyncio.run(main())

async def good_task():
    await asyncio.sleep(2)
    print("good task done")

async def bad_task():
    await asyncio.sleep(1)
    raise Exception("bad task error")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(good_task())
            tg.create_task(bad_task())
    except Exception as e:
        print(f"Ошибка: {e}")

#asyncio.run(main())

async def add(a, b):
    await asyncio.sleep(1)
    return a + b

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(add(1, 2))
        t2 = tg.create_task(add(3, 4))
    print("Результаты:", t1.result(), t2.result())

#asyncio.run(main())

async def fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.text()

async def main():
    urls = [
        # "https://python.org",
        # "https://google.com",
        # "https://yandex.ru",
        # "https://microsoft.com",
        # "https://apple.com",
        # "https://ibm.com",
        # "https://oracle.com",
        # "https://httpbin.org/delay/2",
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
    ]
    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.TaskGroup() as tg:
                tasks = [tg.create_task(fetch(session, url)) for url in urls]
                for task in tasks:
                    print("длина ответа:", len(task.result()))
    except Exception as e:
        print(f"Ошибка: {e}")
    else:
        for task in tasks:
            print("длина ответа:", len(task.result()))

#asyncio.run(main())

async def bad_task1():
    raise ValueError("bad task error1")

async def bad_task2():
    raise RuntimeError("bad task error2")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(bad_task1())
            tg.create_task(bad_task2())
    except* ValueError as e:
        print(f"Ошибка ValueError: {e}")

    except* RuntimeError as e:
        print(f"Ошибка RuntimeError: {e}")

#asyncio.run(main())


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

async def main():
    urls = [
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/1",
        "https://nonexistent.domain",
    ]

    try:
        async with asyncio.TaskGroup() as tg:
            for url in urls:
                tg.create_task(fetch(url))

    except* aiohttp.ClientResponseError as e:
        print(f"Ошибка ответа сервиса: {e}")

    except* aiohttp.ClientConnectorError as e:
        print(f"Ошибка подключения: {e}")

#asyncio.run(main())

async def div(a, b):
    await asyncio.sleep(0.5)
    return a / b

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(div(10, 2))
            t2 = tg.create_task(div(10, 0))
            t3 = tg.create_task(div(11, 0))
            t4 = tg.create_task(div(10, 1))
    except* ZeroDivisionError as e:
        print(f"Ошибка деления на ноль: {e}")

#asyncio.run(main())

"""
Вы — разработчик сервиса, который должен параллельно выполнять несколько сетевых и вычислительных задач. 
Вам нужно:

Создать асинхронные функции:
fetch_url(url) — делает HTTP-запрос к указанному адресу (через aiohttp). 
Если сервер возвращает ошибку (например, 404), это должно приводить к исключению.
compute_division(a, b) — выполняет деление a / b с искусственной задержкой (asyncio.sleep). 
Если b == 0, возникает ZeroDivisionError.

В функции main:
Создайте список URL, в котором будут как корректные сайты (например, https://httpbin.org/get), 
так и некорректные (например, https://httpbin.org/status/404, https://nonexistent.domain).
Запустите параллельно несколько задач: загрузку страниц (fetch_url) 
и несколько вычислений (compute_division) с разными параметрами.
Используйте TaskGroup для управления задачами.

Реализуйте обработку ошибок:
Если при загрузке страниц произойдёт ошибка, её нужно поймать с помощью except* aiohttp.ClientError.
Если при делении произойдёт ошибка, её нужно поймать с помощью except* ZeroDivisionError.
Для каждой пойманной ошибки выведите сообщение с её описанием.
Убедитесь, что при падении нескольких задач вы видите все ошибки, а не только первую.
"""

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
            print(f'Получен ответ от {url}: длина {len(text)}')

async def compute_division(a, b):
    await asyncio.sleep(0.5)
    result = a / b
    print(f'Результат деления {a} / {b}: {result}')
    return result

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
        "https://nonexistent.domain",
    ]

    try:
        async with asyncio.TaskGroup() as tg:
            for url in urls:
                tg.create_task(fetch_url(url))

            tg.create_task(compute_division(11, 2))
            tg.create_task(compute_division(11, 0))
            tg.create_task(compute_division(10, 0))

    except* aiohttp.ClientError as e:
        print(f"Ошибка сети или HTTP: {e}")

    except* ZeroDivisionError as e:
        print(f"Ошибка деления на ноль: {e}")

#asyncio.run(main())


async def worker():
    try:
        print("Начинаю работу")
        await asyncio.sleep(5)
        print("Работа завершена")
    except asyncio.CancelledError:
        print("Работа отменена")
        raise

async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")
    
#asyncio.run(main())


async def worker_with_cleanup():
    try:
        print("открываю ресурс")
        await asyncio.sleep(10)
        print("работа выполнена")
    except asyncio.CancelledError:
        raise

    finally:
        print("задача отменена, закрываю реусрс")

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            for i in range(10):
                await asyncio.sleep(1)
                print(f"запрос {url} выполняется {i} раз")
            print(f"запрос {url} завершен")

    finally:
        print(f"закрываю соединение с {url}")

async def main():
    urls = [
        "https://httpbin.org/delay/3",
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/5",
    ]
    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.TaskGroup() as tg:
                for url in urls:
                    tg.create_task(fetch(session, url))

    except* aiohttp.ClientError as e:
        for exc in e.exceptions:
            print(f"Ошибка сети или HTTP: {exc}")

    except* asyncio.CancelledError as e:
        print("Оставшиеся задачи отменены")

#asyncio.run(main())


"""
Вы создаёте программу, которая:
Загружает данные с нескольких URL (некоторые URL корректные, некоторые вызывают ошибки).
Параллельно выполняет вычисления (например, деление чисел, где могут возникнуть ошибки деления на ноль).
Использует TaskGroup для управления всеми задачами.
Корректно собирает все ошибки в ExceptionGroup.
Гарантирует, что при падении одной задачи остальные корректно отменяются, а ресурсы освобождаются.
urls = [
    "https://httpbin.org/get",        # корректный
    "https://httpbin.org/status/404", # вызовет ошибку 404
    "https://httpbin.org/delay/5",    # имитация долгой загрузки
]

Создайте функцию async fetch_url(session, url), которая:
Загружает страницу с помощью aiohttp.
Если URL возвращает ошибку, она выбрасывается наружу (не ловим внутри).
В блоке finally закрываем соединение (или выводим сообщение о завершении).

Создайте функцию async compute_division(a, b), которая:
Выполняет a / b.
Если b == 0, выбрасывается ZeroDivisionError.
Использует await asyncio.sleep(...) для имитации долгих вычислений.
В блоке finally печатает, что вычисление завершено.

В main() используйте asyncio.TaskGroup для запуска:
Задач на загрузку URL.
Задач на вычисления (например, деление нескольких чисел, где есть деление на ноль).
Оберните TaskGroup в блок try/except* для обработки ошибок:
except* aiohttp.ClientError → вывод ошибок HTTP.
except* ZeroDivisionError → вывод ошибок деления на ноль.
except* asyncio.CancelledError → вывод, что оставшиеся задачи были отменены.

Убедитесь, что:
Если одна задача падает, остальные отменяются.
В finally каждой задачи всегда выполняется очистка/закрытие ресурсов.
Все ошибки собираются и выводятся после завершения TaskGroup.
"""

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            for i in range(5):
                await asyncio.sleep(1)
                print(f"запрос {url} выполняется {i} раз")
            print(f"запрос {url} завершен")

    finally:
        print(f"закрываю соединение с {url}")

async def compute_division(a, b):
    try:
        await asyncio.sleep(2)
        result = a / b
        print(f"вычисление {a} / {b} завершено с результатом {result}")
    finally:
        print(f"вычисление {a} / {b} завершено")

async def main():
    urls = [
        "https://httpbin.org/get",        # корректный
        "https://httpbin.org/status/404", # вызовет ошибку 404
        "https://httpbin.org/delay/5",    # имитация долгой загрузки
    ]

    divisions = [
        (10, 2),
        (5, 0),
        (10, 0),
    ]

    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.TaskGroup() as tg:
                for url in urls:
                    tg.create_task(fetch_url(session, url))

                for a, b in divisions:
                    tg.create_task(compute_division(a, b))

    except* aiohttp.ClientError as e:
        for exc in e.exceptions:
            print(f"Ошибка сети или HTTP: {exc}")

    except* ZeroDivisionError as e:
        for exc in e.exceptions:
            print(f"Ошибка деления на ноль: {exc}")
            
    except* asyncio.CancelledError as e:
        print("Оставшиеся задачи отменены")

#asyncio.run(main())


"""
asyncio.timeout()

async with asyncio.timeout(5):
    await some_coroutine()

try:
    data = await fetch(url)
"""

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with asyncio.timeout(3):
            async with session.get(url) as response:
                return await response.text()

"""
try:
    data = await fetch("https://httpbin.org/delay/5")
except asyncio.TimeoutError:
    print("Время ожидания истекло")

async with asyncio.timeout(4):
    async with asyncio.TaskGroup() as tg:
        tg.create_task(fetch("https://httpbin.org/delay/5"))
        tg.create_task(fetch("https://httpbin.org/get"))
"""

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with asyncio.timeout(3):
                async with session.get(url) as response:
                    return await response.text()
        finally:
            print(f"закрываю соединение с {url}")

# async with asyncio.timeout(6):
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(fetch("https://httpbin.org/delay/5"))
#         tg.create_task(fetch("https://httpbin.org/get"))
#         tg.create_task(compute_division(10, 0))
#         tg.create_task(compute_division(10, 0))

async def long_task(name):
    for i in range(10):
        await asyncio.sleep(1)
        print(f"{name} выполняется {i} раз")

async def main():
    async with asyncio.timeout(15):
        async with asyncio.TaskGroup() as tg:
            tg.create_task(long_task("Первая задача"))
            tg.create_task(long_task("Вторая задача"))

#asyncio.run(main())

async def fetch(session, url):
    async with asyncio.timeout(3):
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

async def main():
    urls = [
        "https://httpbin.org/delay/5",
        "https://httpbin.org/delay/2",
    ]
    async with aiohttp.ClientSession() as session:
        try:
            async with asyncio.timeout(10):
                async with asyncio.TaskGroup() as tg:
                    for url in urls:
                        tg.create_task(fetch(session, url))

        # except* asyncio.TimeoutError as e:
        #     for exc in e.exceptions:
        #         print(f"Таймаут подзадачи: {exc}")

        # except* asyncio.exceptions.CancelledError:
        #     print("Оставшиеся задачи отменены")

        except* Exception as e:
            print(type(e))
            for exc in e.exceptions:
                print(f"Ошибка: {exc}")
                print(type(exc))

#asyncio.run(main())

"""
Загружать данные с нескольких URL параллельно.
Выполнять вычисления (например, деление чисел, где может возникнуть ZeroDivisionError).
Использовать локальные таймауты для каждой подзадачи (например, 3 секунды).
Использовать глобальный таймаут для всей группы задач (например, 10 секунд).
Обрабатывать ошибки через ExceptionGroup:
aiohttp.ClientError для сетевых ошибок.
ZeroDivisionError для вычислений.
asyncio.TimeoutError для превышения таймаута подзадачи.
Гарантировать, что после отмены задач выполняется finally, чтобы закрыть соединения или завершить вычисления.
"""

import asyncio
import aiohttp


async def worker(session, url):
    try:
        async with asyncio.timeout(3):
            print('[Worker] Загрузка:', url)
            async with session.get(url) as response:
                response.raise_for_status()
                print('[Worker] Загружен:', url,)
                return await response.text()
    finally:
        print('[Finally] Ресурсы освобождены:', url)


async def division(a, b):
    try:
        async with asyncio.timeout(3):
            result = a / b
            print(f'[Division] Выполнение деления {a} / {b} с результатом {result}')
            return result
    finally:
        print(f'[Finally] Деление {a} / {b} завершено')


async def main():
    urls = [
        'https://example.com',
        "https://httpbin.org/delay/5",
        "https://httpbin.org/delay/2",
    ]
    numbers = [
        (1, 2),
        (3, 0),
        (4, 5),
        (6, 0),
    ]

    try:
        async with aiohttp.ClientSession() as session:
            async with asyncio.timeout(10):
                async with asyncio.TaskGroup() as tg:
                    for url in urls:
                        tg.create_task(worker(session, url))
                    for a, b in numbers:
                        tg.create_task(division(a, b))

    except* aiohttp.ClientError as e:
        for exs in e.exceptions:
            print('[Ошибка]:', exs)

    except* ZeroDivisionError as e:
        for exs in e.exceptions:
            print('[Ошибка]:', exs)

    except* asyncio.TimeoutError as e:
        for exs in e.exceptions:
            print('[Ошибка]:', exs)

    finally:
        print('[Finally] Выполнение закончено. Все ресурсы освобождены.')

#asyncio.run(main())
 
#fan out fan in
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/404",
    ]

    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(url)) for url in urls]

    except* aiohttp.ClientError as e:
        print(f"Ошибка сети или HTTP: {e}")

    for task in tasks:
        if task.done() and not task.cancelled() and task.exception() is None:
            print("Результат:", len(task.result()))

#asyncio.run(main())

#done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

async def producer():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Производитель: {i}")
        yield i

async def processor(aiter):
    async for item in aiter:
        await asyncio.sleep(0.5)
        result = item * 2
        print(f"Процессор: {result}")
        yield result

async def consumer(aiter):
    async for item in aiter:
        print(f"Потребитель: {item}")

async def main():
    data = producer()
    processed = processor(data)
    await consumer(processed)

#asyncio.run(main())

import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Производитель: {i}")
        await queue.put(i)
    await queue.put(None)

async def processor(in_q, out_q):
    while True:
        item = await in_q.get()
        if item is None:
            await out_q.put(None)
            break
        result = item * 2
        await asyncio.sleep(0.5)
        print(f"Процессор: {result}")
        await out_q.put(result)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Потребитель: {item}")

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(producer(q1))
        tg.create_task(processor(q1, q2))
        tg.create_task(consumer(q2))

#asyncio.run(main())

"""
async with asyncio.TaskGroup() as tg:
    tg.create_task(producer(q1)
    for _ in range(3):
        tg.create_task(processor(q1, q2))
    tg.create_task(consumer(q2))
"""

async def safe_fetch(url):
    try: 
        async with asyncio.timeout(3):
            return await fetch(url)
    except asyncio.TimeoutError:
        print(f"Запрос {url} превысил время ожидания")
        return None

#semaphore = asyncio.Semaphore(3)
"""
async with semaphore:
    #...
"""

async def worker(name, semaphore):
    async with semaphore:
        print(f"Начало работы {name}")
        await asyncio.sleep(2)
        print(f"Завершение работы {name}")

async def main():
    semaphore = asyncio.Semaphore(2)
    async with asyncio.TaskGroup() as tg:
        for i in range(5):
            tg.create_task(worker(f"Worker {i}", semaphore))

#asyncio.run(main())

async def fetch(url, session, semaphore):
    async with semaphore:
        print(f"Запрашиваю {url}")
        async with session.get(url) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    urls = [f"https://httpbin.org/delay/1?i={i}" for i in range(10)]
    semaphore = asyncio.Semaphore(3)
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(url, session, semaphore)) for url in urls]

#asyncio.run(main())

"""
Вам нужно реализовать асинхронную программу, которая:
Загружает содержимое с нескольких URL-адресов (например, страницы https://httpbin.org/delay/X, где X — это задержка).
Одновременно выполняет не более трёх запросов. Для ограничения используйте asyncio.Semaphore.

Для каждого успешно завершённого запроса выводит сообщение вида:
Успешно загружено: <url>, длина ответа = <число символов>

Если при загрузке возникает ошибка (aiohttp.ClientError или таймаут), нужно обработать её и вывести сообщение:
Ошибка при загрузке: <url>, причина: <текст ошибки>

После завершения всех запросов программа должна вывести общее количество успешно обработанных URL и количество ошибок.
"""

async def fetch_url(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                text = await response.text()
                print(f"Успешно загружено: {url}, длина ответа = {len(text)}")
                return True
        except aiohttp.ClientError as e:
            print(f"Ошибка при загрузке: {url}, причина: {e}")
            return False
        except asyncio.TimeoutError:
            print(f"Ошибка при загрузке: {url}, причина: таймаут")
            return False

async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/1",
        "https://not-exist.domain",
        'https://httpbin.org/delay/5',
        'https://github.com',
    ]

    semaphore = asyncio.Semaphore(3)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    sucsess = sum(1 for result in results if result)
    errors = len(results) - sucsess
    print(f"Успешно загружено: {sucsess}, ошибка: {errors}")



import re

semaphore = asyncio.Semaphore(3)

async def fetch_url(session, url):
    async with semaphore:
        async with session.get(url) as resp:
            text = await resp.text()
            print(f"Загржуено: {url} (длина {len(text)})")
            return text

async def process_text(text):
    words = re.findall(r"\w+", text.lower())
    await asyncio.sleep(0.01)
    print(f"Обработка текста: {len(words)} слов")
    return len(words)

async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        #"https://httpbin.org/status/404",
        "https://httpbin.org/delay/1",
        #"https://not-exist.domain",
        'https://httpbin.org/delay/5',
        'https://github.com',
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in urls]

        process_tasks = []
        for task in tasks:
            text = await task
            process_tasks.append(asyncio.create_task(process_text(text)))

        results = await asyncio.gather(*process_tasks, return_exceptions=True)

    total_words = sum(results)
    print(f"Всего слов: {total_words}")

#asyncio.run(main())


async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Производитель положил: {i}")
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Потребитель получил: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=3)

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await queue.join()
    consumer_task.cancel()

#asyncio.run(main())


import random

async def producer(queue, name):
    for i in range(3):
        item = f"{name}-{i}"
        await queue.put(item)
        print(f"Производитель {name} положил: {item}")
        await asyncio.sleep(random.uniform(0.1, 1))

async def consumer(queue, name):
    while True:
        item = await queue.get()
        print(f"Потребитель {name} получил: {item}")
        await asyncio.sleep(random.uniform(0.1, 1))
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    producers = [
        asyncio.create_task(producer(queue, f"Производитель {i + 1}"))
        for i in range(2)
    ]

    consumers = [
        asyncio.create_task(consumer(queue, f"Потребитель {i + 1}"))
        for i in range(3)
    ]

    await asyncio.gather(*producers)
    await queue.join()
    for c in consumers:
        c.cancel()

#asyncio.run(main())

"""
асинхронная обработка данных через очередь 

producer consumer
2-3 производителя генерируют "данные-1"...
кладут в очередь с задержкой

потребители извлекают и обрабатывают данные с задержкой

очередь maxsize=5

join
task_done
cancel

итоговая статистика
"""

async def producer(queue, name, count):
    for i in range(1, count + 1):
        item = f"данные-{i}"
        await queue.put(item)
        print(f"{name} добавил в очередь {item}")
        await asyncio.sleep(random.uniform(0.5, 1.5))

async def consumer(queue, name):
    while True:
        item = await queue.get()
        processed = item.upper()
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f"{name} обработал {item} и получил {processed}")
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=5)

    producers = [
        asyncio.create_task(producer(queue, f"Производитель-1", 5)),
        asyncio.create_task(producer(queue, f"Производитель-2", 5)),
    ]

    consumers = [
        asyncio.create_task(consumer(queue, f"Потребитель-1")),
        asyncio.create_task(consumer(queue, f"Потребитель-2")),
        asyncio.create_task(consumer(queue, f"Потребитель-3")),
    ]

    await asyncio.gather(*producers)

    await queue.join()

    for c in consumers:
        c.cancel()

    print("Все задачи выполнены.")

counter = 0
lock = asyncio.Lock()

async def increment(name):
    global counter
    for _ in range(5):
        async with lock:
            value = counter
            await asyncio.sleep(0.1)
            counter = value + 1
            print(f"{name} увеличил счетчик на 1 ({counter})")

async def main():
    await asyncio.gather(
        increment("Поток 1"),
        increment("Поток 2"),
    )

#asyncio.run(main())

event = asyncio.Event()

async def waiter(name):
    print(f"{name} ожидает события...")
    await event.wait()
    print(f"{name} получил событие!")

async def setter():
    await asyncio.sleep(2)
    print("Событие готово!")
    event.set()

async def main():
    await asyncio.gather(
        waiter("Поток 1"),
        waiter("Поток 2"),
        setter(),
    )

#asyncio.run(main())


queue = []
condition = asyncio.Condition()

async def producer():
    for i in range(5):
        async with condition:
            queue.append(i)
            print(f"Производитель добавил {i} в очередь")
            condition.notify()
        await asyncio.sleep(1)

async def consumer(name):
    while True:
        async with condition:
            await condition.wait_for(lambda: len(queue) > 0)
            item = queue.pop(0)
            print(f"Потребитель {name} получил {item} из очереди")
        await asyncio.sleep(0.4)

async def main():
    consumers = [asyncio.create_task(consumer(f"Потребитель-{i+1}")) for i in range(3)]
    await producer()
    for c in consumers:
        c.cancel()

#asyncio.run(main())

async def producer(queue):
    for i in range(100):
        print(f"Производитель добавил {i} в очередь")
        await queue.put(i)
        await asyncio.sleep(0.01)

async def consumer(queue):
    while True:
        item = await queue.get()
        await asyncio.sleep(0.1)
        print(f"Потребитель получил {item} из очереди")
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=10)
    await asyncio.gather(
        producer(queue),
        consumer(queue),
    )

#asyncio.run(main())

semaphore = asyncio.Semaphore(3)

async def fetch(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.text()

async def process(item):
    try:
        async with asyncio.timeout(1):
            await asyncio.sleep(2)
    except asyncio.TimeoutError:
        print(f"Время ожидания истекло для {item}")

queue = asyncio.Queue(maxsize=5)
event = asyncio.Event()

async def producer():
    for i in range(10):
        await queue.put(i)
        print(f"Производитель добавил {i} в очередь")
        if queue.full():
            print("Очередь заполнена")
            await event.wait()
            event.clear()

async def consumer():
    while True:
        item = await queue.get()
        print(f"Потребитель получил {item} из очереди")
        await asyncio.sleep(0.1)
        event.set()
        queue.task_done()


"""
асинхронная обработка данных с управлением backpressure

производитель-потребитель

производители генерируют "данные-1"... со случайной задержкой
    если очередь заполнена, то потребитель ждет

потребители извлекают данные из очереди и обрабатывают их за случайное время
    lock для общего счетчика обработанных данных

event для сигнализации об окончании заполнения очереди производителями
потребители после обработки всех элементов очереди завершатся

condition при освобождении места в очереди уведомлять ожидающих потребителей

итоговая статистика
"""
async def producer(queue, condition, name, count):
    for i in range(1, count + 1):
        item = f"{name}-данные-{i}"

        async with condition:
            while queue.full():
                print(f"{name} ждет освобождения места в очереди")
                await condition.wait()

        await queue.put(item)
        print(f"{name} добавил в очередь {item}")
        await asyncio.sleep(random.uniform(0.5, 1.5))

    print(f"{name} завершил работу")

async def consumer(queue, lock, event, condition, name, stats):
    while True:
        if queue.empty() and event.is_set():
            break

        try: 
            item = await asyncio.wait_for(queue.get(), timeout=1)

        except asyncio.TimeoutError:
            continue

        await asyncio.sleep(random.uniform(0.5, 1.5))
        processed = item.upper()
        print(f"{name} обработал {item} -> {processed}")

        async with lock:
            stats[name] = stats.get(name, 0) + 1

            queue.task_done()

            async with condition:
                condition.notify()

    print(f"{name} завершил работу")

async def main():
    queue = asyncio.Queue(maxsize=5)
    lock = asyncio.Lock()
    event = asyncio.Event()
    condition = asyncio.Condition()

    stats = {}

    producers = [
        asyncio.create_task(producer(queue, condition, f"Производитель-{i}", 5)) for i in range(2)
    ]
    consumers = [
        asyncio.create_task(consumer(queue, lock, event, condition, f"Потребитель-{i}", stats)) for i in range(2)
    ]

    await asyncio.gather(*producers)
    event.set()
    await queue.join()
    await asyncio.gather(*consumers)
    print(f"Итоговая статистика:")
    for name, count in stats.items():
        print(f"{name}: обработано {count} элементов")

"""
import requests
resp = requests.get("https://www.google.com")
print(resp.text)
"""

#import aiohttp
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.google.com") as resp:
            text = await resp.text()
            print(text)

#asyncio.run(main())


sem = asyncio.Semaphore(3)

async def fetch(session, url):
    async with sem:
        try: 
            async with session.get(url, timeout=5) as response:
                data = await response.json()
        except asyncio.ClientError as e:
            print(f"Ошибка клиента: {e}")
        except asyncio.TimeoutError:
            print(f"Таймаут для {url}")
        

async def main():
    urls = [
        "https://www.google.com",
        "https://www.yandex.ru",
        "https://www.python.org"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        for r in results:
            print(len(r))

#asyncio.run(main())

import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.google.com")
        print(response.text)

#asyncio.run(main())

async def fetch(client, url):
    r = await client.get(url)
    return r.text

async def main():
    urls = [
        "https://www.google.com",
        "https://www.yandex.ru",
        "https://www.python.org"
    ]
    timeout = httpx.Timeout(5.0, connect=10.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks = [fetch(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for r in results:
            print(len(r))

#asyncio.run(main())

"""
Вам нужно написать программу, которая будет скачивать содержимое нескольких веб-страниц и сравнивать скорость выполнения при использовании:
Синхронного клиента requests.
Асинхронного клиента aiohttp.
Асинхронного клиента httpx.
Список адресов возьмите следующий:

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
]

Реализовать три функции:
fetch_requests(urls) — выполняет загрузку всех страниц синхронно через requests.
fetch_aiohttp(urls) — выполняет загрузку всех страниц параллельно через aiohttp.
fetch_httpx(urls) — выполняет загрузку всех страниц параллельно через httpx.

Для каждой функции измерить время выполнения (time.time() или asyncio.get_event_loop().time()).
Сравнить результаты: какой способ оказался самым быстрым.

Обработать возможные ошибки:
таймаут,
сетевые ошибки (ClientError у aiohttp, httpx.RequestError у httpx).

Итоговый вывод должен содержать таблицу или список
"""

import requests
#import aiohttp
#import httpx
#import asyncio
import time

def fetch_requests(urls):
    start_time = time.time()
    results = []
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            text = response.text
            results.append(len(text))
            print(f"requests Загружено {url}: {len(text)}")

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса {url}: {e}")
    end_time = time.time()
    return end_time - start_time, results

async def fetch_one_aiohttp(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            text = await response.text()
            print(f"aiohttp Загружено {url}: {len(text)}")
            return len(text)
    except aiohttp.ClientError as e:
        print(f"Ошибка запроса {url}: {e}")
    except asyncio.TimeoutError:
        print(f"Таймаут для {url}")

async def fetch_aiohttp(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one_aiohttp(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        end_time = time.time()
        return end_time - start_time, results

async def fetch_one_httpx(client, url):
    try:
        response = await client.get(url, timeout=10)
        response.raise_for_status()
        text = response.text
        print(f"httpx Загружено {url}: {len(text)}")
        return len(text)

    except httpx.RequestError as e:
        print(f"Ошибка запроса {url}: {e}")
    except asyncio.TimeoutError:
        print(f"Таймаут для {url}")
    except httpx.HTTPStatusError as e:
        print(f"httpx ошибка при загрузке {url}: {e}")

async def fetch_httpx(urls):
    start_time = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one_httpx(client, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    end_time = time.time()
    return end_time - start_time, results

async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]

    time_requests, _ = fetch_requests(urls)
    time_aiohttp, _ = await fetch_aiohttp(urls)
    time_httpx, _ = await fetch_httpx(urls)

    print(f"Время выполнения requests: {time_requests:.2f} секунд")
    print(f"Время выполнения aiohttp: {time_aiohttp:.2f} секунд")
    print(f"Время выполнения httpx: {time_httpx:.2f} секунд")

#asyncio.run(main())

"""
aiohttp.ClientConnectorError
aiohttp.ClientPayloadError
aiohttp.ClientResponseError
try:
    async with session.get(url, timeout=10) as response:
        data = await response.json()
except aiohttp.ClientError as e:
    print(f"Ошибка клиента {url}: {e}")

except asyncio.TimeoutError:
    print(f"Таймаут для {url}")

async with aiohttp.ClientSession(headers={"User-Agent": "Mozilla/5.0"}) as session:
    async with session.get(url, timeout=10) as response:

async def download_file(session, url, filename):
    async with session.get(url) as response:
        with open(filename, "wb") as f:
            while chunk := await response.content.read(1024):
                f.write(chunk)
"""

from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def fetch(client, url):
    print("запускаю")
    r = await client.get(url)
    r.raise_for_status()
    return r.text

async def main():
    async with httpx.AsyncClient() as client:
        text = await fetch(client, "https://httpbin.org/status/500")
        print(text)

#asyncio.run(main())

# async with httpx.AsyncClient() as client:
#     r1 = await client.get("https://httpbin.org/cookies/set?foo=bar")
#     r2 = await client.get("https://httpbin.org/cookies")
#     print(r2.json()["cookies"])

# headers = {"User-Agent": "Mozilla/5.0"}
# async with httpx.AsyncClient(headers=headers) as client:
#     r = await client.get("https://httpbin.org/headers")
#     print(r.json())

# auth = ("логин", "пароль")
# async with httpx.AsyncClient(auth=auth) as client:
#     r = await client.get("https://httpbin.org/basic-auth/логин/пароль")
#     print(r.status_code)

async def download(url, filename):
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            with open(filename, "wb") as f:
                async for chunk in response.aiter_bytes():
                    f.write(chunk)

# limits = httpx.Limits(max_connections=10, max_keepalive_connections=5)
# async with httpx.AsyncClient(limits=limits) as client:
#     ...

#from myapp import app

async def test_app():
    async with https.AsyncClient(app=app, base_url="http://test") as client:
        r = await client.get("/")
        assert r.status_code == 200

"""
https.ConnectError
httpx.TimeoutException
httpx.HTTPStatusError

try:
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        r.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"httpx ошибка при загрузке {url}: {e}")
"""


"""
Вам необходимо реализовать небольшой асинхронный API-сервис с использованием библиотеки aiohttp.
Сервис должен предоставлять следующие возможности:
Эндпоинт / (GET)
Возвращает приветственное сообщение в формате JSON, например:
{ "message": "Добро пожаловать в наш сервис!" }

Эндпоинт /items (GET)
Возвращает список всех элементов (данные можно хранить в обычном Python-списке в памяти).
Формат ответа:
{ "items": ["item1", "item2", "item3"] }

Эндпоинт /items (POST)
Принимает JSON с полем "name" и добавляет элемент в список.
Пример запроса:
{ "name": "новый_элемент" }

Пример ответа:
{ "message": "Элемент успешно добавлен" }

Эндпоинт /items/{id} (GET)
Возвращает элемент по индексу (например, /items/0 → item1).
Если элемент не найден, возвращает ошибку 404 и JSON с сообщением.
Эндпоинт /items/{id} (DELETE)
Удаляет элемент по индексу.
Возвращает сообщение об успешном удалении или ошибку, если индекс не существует.

Рекомендации по реализации:
Запуск aiohttp-сервера
Подумайте, как мы запускали сервер на aiohttp на лекции.
Вспомните, что используется web.Application() и функция web.run_app(...).

Маршруты
Маршруты (эндпоинты) в aiohttp добавляются через app.router.add_get(...), add_post(...), add_delete(...).
Вспомните, что внутри обработчика запроса мы используем async def.

Возврат JSON-ответа
aiohttp имеет специальную функцию web.json_response(...).
Подумайте, как можно вернуть словарь Python в виде JSON.

Хранение данных
Данные можно хранить в обычном Python-списке, например items = [].
Для простоты храните его прямо в глобальной области видимости.

POST-запрос (добавление элемента)
Для извлечения данных из POST-запроса используйте await request.json().
Подумайте, как из полученного словаря достать поле "name".

GET по индексу (/items/{id})
Чтобы получить индекс из URL, используйте request.match_info["id"].
Не забудьте преобразовать его в int.

Обработка ошибок (404)
Если индекс выходит за пределы списка, верните web.json_response({"error": "Элемент не найден"}, status=404).

DELETE-запрос
Используйте del items[index] для удаления.
Не забудьте обработать ситуацию, если индекс неверный.
"""

from aiohttp import web

items = []

async def get_items(request):
    return web.json_response({"items": items})


async def get_item(request):
    try:
        item_id = int(request.match_info["id"])
        item = items[item_id]
        return web.json_response({"id": item_id, "item": item})
    except (IndexError, ValueError):
        return web.json_response({"error": "Элемент не найден"}, status=404)


async def add_item(request):
    try:
        data = await request.json()
        name = data.get("name")
        if not name:
            return web.json_response({"error": "Поле 'name' обязательно"}, status=400)
        items.append(name)
        return web.json_response({"message": "Элемент успешно добавлен", 'id': len(items) - 1})

    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)


async def delete_item(request):
    try:
        item_id = int(request.match_info["id"])
        deleted = items.pop(item_id)
        return web.json_response({"message": f"Элемент {deleted} успешно удален"})
    except (IndexError, ValueError):
        return web.json_response({"error": "Элемент не найден"}, status=404)


async def init_app():
    app = web.Application()
    app.router.add_get('/items', get_items)
    app.router.add_get('/items/{id}', get_item)
    app.router.add_post('/items', add_item)
    app.router.add_delete('/items/{id}', delete_item)

    return app

# if __name__ == '__main__':
#     web.run_app(init_app(), host='127.0.0.1', port=8088)

"""
таймаут на операцию
таймаут на всю задачу
таймауты на уровне клиента или сервера
"""

async def fetch_data():
    print('начинаем загрузку данных')
    await asyncio.sleep(2)
    print('загрузка данных завершена')

async def main():
    try:
        async with asyncio.timeout(1):
            await fetch_data()
    except asyncio.TimeoutError:
        print('загрузка данных превысила 1 секунду')

# asyncio.run(main())

async def fetch_page(url):
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                return None

async def main():
    try:
        html = await fetch_page('https://example.com')
        print("страница загружена")
    except asyncio.TimeoutError:
        print("загрузка страницы превысила 5 секунд")

# asyncio.run(main())

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    connection = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connection) as session:
        urls = ['https://example.com'] * 20
        tasks = [fetch_page(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(f"загружено страниц: {len(results)}")

#asyncio.run(main())

async def fetch_with_timeout(session, url):
    try:
        async with asyncio.timeout(5):
            async with session.get(url) as response:
                return await response.text()
    except asyncio.TimeoutError:
        return 'timeout'

async def main():
    connection = aiohttp.TCPConnector(limit=10)
    timeout = aiohttp.ClientTimeout(connect=2, sock_read=3)

    async with aiohttp.ClientSession(connector=connection, timeout=timeout) as session:
        urls = ['https://example.com'] * 15
        tasks = [fetch_with_timeout(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

#asyncio.run(main())

from aiohttp import WSMsgType, WSCloseCode
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def connect_websocket(session, url):
    return await session.ws_connect(
        url,
        heartbeat=30.0,
        timeout=10.0
    )

async def handle_messages(ws, outgoing_queue):
    async def receive_messages():
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                logger.info(f"Получено сообщение: {msg.data}")

            elif msg.type == WSMsgType.BINARY:
                logger.info(f"Получено бинарное сообщение: {len(msg.data)} байт")

            elif msg.type == WSMsgType.CLOSED:
                logger.info("Соединение закрыто")
                break

            elif msg.type == WSMsgType.ERROR:
                logger.error("Ошибка соединения", ws.exception())
                break

    async def send_messages():
        while not ws.closed:
            try:
                msg = await asyncio.wait_for(outgoing_queue.get(), timeout=1.0)
                if not ws.closed:
                    await ws.send_str(msg)
                    logger.info(f"Отправлено сообщение: {msg}")
            except asyncio.TimeoutError:
                continue

    await with asyncio.TaskGroup() as tg:
        tg.create_task(receive_messages())
        tg.create_task(send_messages())

async def maintain_websocket(url, shutdown_event):
    sesion = None
    retry_delay = 1.0
    max_retry_delay = 60.0
    outgoing_queue = asyncio.Queue()

    try:
        sessoin = aiohttp.ClientSession()

        while not shutdown_event.is_set():
            try:
                logger.info(f"Подключение к {url}")
                ws = await connect_websocket(session, url)
                logger.info(f"Соединение установлено")

                retry_delay = 1.0

                await handle_messages(ws, outgoing_queue)

                if not ws.closed:
                    await ws.close(code=WSCloseCode.GOING_AWAY, message="Соединение закрыто")

            except aiohttp.WSServerHandshakeError as e:
                logger.error(f"Ошибка handshake: {e}")
            except aiohttp.ClientError as e:
                logger.error(f"Ошибка клиента: {e}")
            except asyncio.TimeoutError:
                logger.error(f"Таймаут соединения превышен")
            except Exception as e:
                logger.error(f"Произошла ошибка: {e}", exc_info=True)

            if shutdown_event.is_set():
                break
            
            logger.info(f"Переподключение через {retry_delay} секунд")
            try:
                await asyncio.wait_for(shutdown_event.wait(), timeout=retry_delay)
                break
            except asyncio.TimeoutError:
                pass

            retry_delay = min(retry_delay * 2, max_retry_delay)

    finally:
        if session:
            await session.close()
        logger.info("Соединение с сервером закрыто")


async def main():
    shutdown_event = asyncio.Event()

    def signal_handler():
        logger.info("Получено сигнал завершения")
        shutdown_event.set()

    loop = asyncio.get_event_loop()
    for sig in {signal.SIGINT, signal.SIGTERM}:
        loop.add_signal_handler(
            sig,
            functools.partial(signal_handler)
        )
    
    url = "ws://localhost:8088/ws"

    try:
        await maintain_websocket(url, shutdown_event)
    finally:
        logger.info("Завершение работы")

async def producer(outgoing_queue, shutdown_event):
    counter = 0

    while not shutdown_event.is_set():
        await asyncio.sleep(5)
        message = f"Сообщение {counter}"
        await outgoing_queue.put(message)
        counter += 1


"""
Необходимо написать асинхронное приложение, которое:
Загружает данные с нескольких API-эндпоинтов (список URL будет задан).
Делает это конкурентно (параллельно с помощью корутин).
Использует пул соединений для экономии ресурсов.
Устанавливает таймауты на каждый запрос, чтобы избежать зависаний.
Собирает результаты всех успешных запросов в единый список (или файл JSON) и выводит статистику:
количество успешных ответов;
количество ошибок (например, таймаутов или HTTP-ошибок);
среднее время отклика.

2. Исходные данные
Пример списка тестовых URL (можно использовать публичные API или заглушки):
URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    # … добавьте ещё 10–15 URL для нагрузки
]

3. Требования к реализации
Выберите клиент:
либо aiohttp,
либо httpx в асинхронном режиме.

Настройте пул соединений:
например, ограничьте количество одновременных подключений (5–10).

Настройте таймауты:
общий таймаут на выполнение запроса (например, 5 секунд),
таймаут на подключение (например, 2 секунды).

Реализуйте обработку ошибок:
отлавливайте TimeoutError и ошибки HTTP (4xx, 5xx),
учитывайте их в статистике.
Используйте конкурентное выполнение (asyncio.gather или TaskGroup).

По завершении работы:
сохраните успешные ответы в JSON-файл,
выведите статистику (успехи, ошибки, среднее время отклика).
"""