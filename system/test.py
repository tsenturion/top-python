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

import asyncio
import aiohttp
import random
import time

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

asyncio.run(main())