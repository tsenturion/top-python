import asyncio
import asyncpg
import pytest
from unittest.mock import AsyncMock, patch


async def fetch_data():
    return [5, 15, 25, 3]

async def process_data():
    try:
        data = await fetch_data()
        return [x for x in data if x > 10]
    except TimeoutError:
        return []

async def add_with_delay(a, b, delay=0.5):
    await asyncio.sleep(delay)
    return a + b


async def divide(a, b):
    await asyncio.sleep(0.1)
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


async def insert_user(conn, name):
    await conn.execute("INSERT INTO users (name) VALUES ($1)", name)