"""
IsolatedAsyncioTestCase
"""

import asyncio
import unittest
from unittest.mock import patch, AsyncMock
import pytest

class MyAsyncTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.resource = await asyncio.sleep(0, result="initialized")

    async def asyncTearDown(self):
        self.resource = None

    async def test_example(self):
        result = await asyncio.sleep(0, result=42)
        self.assertEqual(result, 42)


class TaskTests(unittest.IsolatedAsyncioTestCase):
    async def test_task_completion(self):
        async def coro():
            await asyncio.sleep(0.1)
            return "done"
        
        task = asyncio.create_task(coro())
        result = await asyncio.wait_for(task, timeout=1)
        self.assertEqual(result, "done")


class ExceptionTests(unittest.IsolatedAsyncioTestCase):
    async def test_exception(self):
        async def fail_coro():
            await asyncio.sleep(0.1)
            raise ValueError("Test error")
        
        with self.assertRaises(ValueError) as context:
            await fail_coro()
        self.assertEqual(str(context.exception), "Test error")
            

class DatabaseTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.conn = await self.create_connection()

    async def asyncTearDown(self):
        await self.conn.close()
    
    async def create_connection(self):
        await asyncio.sleep(0.1)
        return "connection"

    async def test_connection(self):
        self.assertEqual(self.conn, "connection")


class TaskGroupTests(unittest.IsolatedAsyncioTestCase):
    async def test_taskgroup(self):
        async def work(i):
            await asyncio.sleep(0.05)
            return i * 2
        
        results = []
        async with asyncio.TaskGroup() as tg:
            for i in range(3):
                tg.create_task(self.collect(work(i), results))
        self.assertEqual(results, [0, 2, 4])

        async def collect(self, coro, results):
            result = await coro
            results.append(result)


async def fetch_data():
    return {"status": 200, "data": [1, 2, 3]}

async def process_data():
    data = await fetch_data()
    return data['data']

async def test_process_data():
    with patch('__main__.fetch_data', new_callable=AsyncMock) as mocked_fetch:
        mocked_fetch.return_value = {'status': 200, 'data': [1, 2, 3]}
        result = await process_data()
        assert result == [1, 2, 3]
        mocked_fetch.assert_awaited_once()

async def main():
    mocked_fetch = AsyncMock(return_value={"status": 200, "data": [1, 2, 3]})

    result = await mocked_fetch()
    print(result)

    mocked_fetch = AsyncMock(side_effect=TimeoutError("Timeout"))
    try:
        await mocked_fetch()
    except TimeoutError as e:
        print(e)

class DataService:
    async def fetch_data(self):
        return {'status': 200, 'data': [1, 2, 3]}

async def process_service_data(service: DataService):
    data = await service.fetch_data()
    return data['data']

async def test_process_service_data():
    service = DataService()
    with patch.object(service, 'fetch_data', new_callable=AsyncMock) as mocked_method:
        mocked_method.return_value = {'status': 200, 'data': [4, 5, 6]}
        result = await process_service_data(service)
        assert result == [4, 5, 6]
        mocked_method.assert_awaited_once()

async def slow_fetch():
    await asyncio.sleep(1)
    return {'status': 200}

async def main():
    mocked_fetch = AsyncMock(side_effect=slow_fetch)
    result = await mocked_fetch()

    mocked_fetch = AsyncMock(side_effect=[
        {'status': 200, 'data': [1]},
        {'status': 200, 'data': []},
    ])

    first = await mocked_fetch()
    second = await mocked_fetch()


@pytest.mark.asyncio
async def test_process_data_with_patch():
    with patch('__main__.fetch_data', new_callable=AsyncMock) as mocked_fetch:
        mocked_fetch.return_value = {'status': 200, 'data': [7, 8, 9]}
        result = await process_data()
        assert result == [7, 8, 9]


"""
Вы создаёте сервис, который получает данные с внешнего API. Для упрощения API представим в виде асинхронной функции fetch_data.
Создайте функцию process_data, которая:
вызывает fetch_data()
возвращает список только тех элементов, которые больше 10

Напишите тест для функции process_data с помощью pytest-asyncio:
Используйте AsyncMock и patch, чтобы замокать fetch_data.
Проверьте, что process_data корректно обрабатывает возвращаемые данные.
Проверьте, что мок вызывается ровно один раз.

Смоделируйте ситуацию, когда fetch_data выбрасывает исключение TimeoutError и убедитесь, что process_data корректно реагирует.
"""