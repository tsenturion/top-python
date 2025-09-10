"""
асинхронная система загрузки и обработки данных 
корутина-поставщик fetch_data. Имитация asyncio.sleep с разным времен
корутина-обработчик process_data получает реультат загрузки и обрабатывает его. Подсчет символом
все параллельно, с create_task
gather чтобы дождаться всех задач
"""
import asyncio
import random

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

if __name__ == "__main__":
    asyncio.run(main())