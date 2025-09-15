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