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

asyncio.run(main())