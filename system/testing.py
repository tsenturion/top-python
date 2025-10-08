"""
IsolatedAsyncioTestCase
"""

import asyncio
import unittest

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