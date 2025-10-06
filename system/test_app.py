import pytest
import asyncio
import asyncpg
import pytest_asyncio
from app import add_with_delay, divide, insert_user

@pytest.mark.asyncio
async def test_add_with_delay():
    result = await add_with_delay(2, 3, delay=0.1)
    assert result == 5

@pytest.mark.asyncio
async def test_divide_zero():
    with pytest.raises(ValueError):
        await divide(10, 0)


class DummyClient:
    async def connect(self):
        await asyncio.sleep(0.1)
        return True
    
    async def close(self):
        await asyncio.sleep(0.1)

@pytest.fixture
async def client():
    c = DummyClient()
    await c.connect()
    yield c
    await c.close()

@pytest.mark.asyncio
async def test_client_connection(client):
    assert client is not None


@pytest_asyncio.fixture(scope="module")
async def pool():
    p = await asyncpg.create_pool(
        user="postgres",
        database="postgres",
        host="localhost",
        password="admin",
        min_size=2,
        max_size=5
    )
    async with p.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL                           
        )
        """)
              
    yield p
    await p.close()

@pytest.mark.asyncio
async def test_insert_user(pool):
    async with pool.acquire() as conn:
        await conn.execute("TRUNCATE users")       
        await insert_user(pool, "John Doe")
        result = await conn.fetch("SELECT id FROM users WHERE name = $1", "John Doe")
    assert len(result) == 1