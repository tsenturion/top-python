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


@pytest_asyncio.fixture(scope="function")
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
        await conn.execute("TRUNCATE users")
              
    yield p
    await p.close()

@pytest.mark.asyncio
async def test_insert_user(pool):
    async with pool.acquire() as conn:
        await insert_user(pool, "John Doe")
        result = await conn.fetch("SELECT * FROM users WHERE name = $1", "John Doe")
        assert len(result) == 1
        assert 'John Doe' in result[0]["name"]


@pytest.mark.asyncio
async def test_multiple_inserts(pool):
    async with pool.acquire() as conn:
        await insert_user(conn, "John Doe")
        await insert_user(conn, "Jane Doe2")
        await insert_user(conn, "Jane Doe3")
        result = await conn.fetch("SELECT * FROM users")
        assert len(result) == 3


@pytest.mark.asyncio
async def test_insert_empty_name(pool):
    async with pool.acquire() as conn:
        with pytest.raises(asyncpg.exceptions.NotNullViolationError):
            await insert_user(conn, None)

@pytest.mark.asyncio
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, -5, -1)
])
async def test_add_with_delay_param(a, b, expected):
    result = await add_with_delay(a, b, delay=0.01)
    assert result == expected


"""
Настроить пул соединений к базе данных при помощи asyncpg в фикстуре.
Создать таблицу users для хранения пользователей.
Написать тесты с использованием pytest-asyncio для проверки корректности работы с базой данных.
Перед каждым тестом очищать таблицу.
Проверить как корректные операции, так и ошибки.

1. Создание таблицы пользователей:
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

2. Очистка таблицы:
TRUNCATE users;

3. Вставка нового пользователя:
INSERT INTO users (name) VALUES ($1);

4. Выбор всех пользователей:
SELECT * FROM users;

5. Поиск пользователя по имени:
SELECT id FROM users WHERE name = $1;


Создайте тестовый файл test_app.py.
Определите асинхронную фикстуру pool при помощи декоратора
Фикстура должна:
Создавать пул соединений с базой данных.
Выполнять SQL для создания таблицы, если она ещё не создана.
Очищать таблицу перед каждым тестом при помощи TRUNCATE.
Закрывать пул соединений после выполнения всех тестов.

Реализуйте тесты:
Тест 1. Добавление одного пользователя и проверка, что он появился в таблице.
Тест 2. Добавление нескольких пользователей и проверка количества строк.
Тест 3. Попытка добавить пользователя с пустым именем.
"""