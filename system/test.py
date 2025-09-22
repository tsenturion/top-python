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

import asyncio
import aiohttp
import random
import time

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

asyncio.run(main())