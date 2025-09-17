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

async with asyncio.timeout(6):
    async with asyncio.TaskGroup() as tg:
        tg.create_task(fetch("https://httpbin.org/delay/5"))
        tg.create_task(fetch("https://httpbin.org/get"))
        tg.create_task(compute_division(10, 0))
        tg.create_task(compute_division(10, 0))