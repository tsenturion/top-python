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
import asyncio
import aiohttp
import random
import time

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

asyncio.run(main())