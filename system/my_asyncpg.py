import psycopg2

# conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="admin")
# cursor = conn.cursor()
# cursor.execute("SELECT 1;")
# rows = cursor.fetchall()

import asyncpg
import asyncio

async def main():
    conn = await asyncpg.connect(
        user="postgres",
        database="postgres",
        password="admin",
        host="localhost"
    )

    rows = await conn.fetch("SELECT id, username FROM users;")
    for row in rows:
        print(row['id'], row['username'])

    await conn.close()

#asyncio.run(main())

"""
conn:
fetch(query, *args):
fetchrow(query, *args):
fetchval(query, *args):
execute(query, *args):
"""

async def main():
    conn = await asyncpg.connect(
        user="postgres",
        database="postgres",
        password="admin",
        host="localhost"
    )

    await conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INTEGER
        );
    """)

    await conn.execute(
        "INSERT INTO students (name, age) VALUES ($1, $2)",
        "John Doe", 25
    )

    print("Data inserted successfully.")
    await conn.close()

#asyncio.run(main())

async def main():
    conn = await asyncpg.connect(
        user="postgres",
        database="postgres",
        password="admin",
        host="localhost"
    )

    rows = await conn.fetch("SELECT id, name, age FROM students;")
    for row in rows:
        print(f"{row['id']}: {row['name']} ({row['age']} years old)")

        count = await conn.fetchval("SELECT COUNT(*) FROM students;")
        print(f"Total students: {count}")

        await conn.close()

#asyncio.run(main())
"""
INTEGER -> int
TEXT -> str
BOOLEAN -> bool
TIMESTAMP -> datetime.datetime

await conn.execute(
    "INSERT INTO events(name, start_date, end_date) VALUES ($1, $2, $3)",
    "лекция", datetime.now(), datetime.now() + datetime.timedelta(days=1)
)

stmt = await conn.prepare("SELECT * FROM students WHERE age = $1")
rows = await stmt.fetch(25)
"""

async def main():
    try:
        conn = await asyncpg.connect(
            user="postgres",
            database="postgres",
            password="admin",
            host="localhost"
        )

        await conn.execute("SELECT * FROM non_existent_table;")
    except asyncpg.exceptions.UndefinedTableError as e:
        print(e)
    finally:
        await conn.close()
#asyncio.run(main())

async def main():
    pool = await asyncpg.create_pool(
        user="postgres",
        database="postgres",
        password="admin",
        host="localhost",
        max_size=5,
        min_size=2
    )

    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name, age FROM students;")
        print(rows)

    await pool.close()

#asyncio.run(main())

async def fetch_users(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT id, username, email FROM users;")


async def fetch_students(pool):
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT id, name, age FROM students;")


async def main():
    pool = await asyncpg.create_pool(
        user="postgres",
        database="postgres",
        password="admin",
        host="localhost",
        max_size=5,
        min_size=2,
        timeout=3.0
    )

    users_task = asyncio.create_task(fetch_users(pool))
    orders_task = asyncio.create_task(fetch_students(pool))

    users = await users_task
    orders = await orders_task

    print(users)
    print(orders)

    await pool.close()


"""
Вам предстоит создать небольшое асинхронное приложение на Python, которое подключается к базе данных PostgreSQL с помощью пула соединений (asyncpg.create_pool).
Подключится к базе данных PostgreSQL с использованием пула соединений.
Создать таблицу students.
Добавить в таблицу несколько тестовых записей с именами и возрастами студентов.
Прочитать данные из таблицы и вывести их в консоль.
Корректно закрыть пул соединений после завершения работы.

Требования к заданию
Используйте библиотеку asyncpg.
Все операции должны выполняться через пул соединений.
Запросы к базе данных будут даны вам в готовом виде, поэтому знания SQL не требуются.
Программа должна быть написана с использованием асинхронного стиля (async def, await, asyncio.run).
После выполнения программа должна выводить список всех студентов в консоль в понятном формате.

SQL-запрос для создания таблицы:
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL
);

SQL-запрос для добавления данных:
INSERT INTO students (name, age) VALUES ($1, $2);

SQL-запрос для чтения данных:
SELECT id, name, age FROM students;

Создайте новый файл main.py.
Настройте подключение к базе данных с помощью пула соединений.
Реализуйте функции:
для создания таблицы,
для добавления тестовых данных,
для чтения данных из таблицы.
Выведите полученные данные о студентах в консоль.
Закройте пул соединений после завершения работы.
"""

async def create_table(pool):
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                age INT NOT NULL
            );
        """)
        print("Таблица 'students' успешно создана (если её не было).")


async def insert_students(pool):
    students = [
        ("Алиса", 20),
        ("Боб", 22),
        ("Елена", 19),
        ("Дмитрий", 23)
    ]

    async with pool.acquire() as conn:
        for name, age in students:
            await conn.execute(
                "INSERT INTO students (name, age) VALUES ($1, $2);",
                name, age
            )
    print("Тестовые данные добавлены.")


async def fetch_students(pool):
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name, age FROM students;")
        return rows


async def main():
    pool = await asyncpg.create_pool(
        user="postgres",
        password="admin",
        database="postgres",
        host="localhost",
        min_size=2,
        max_size=5
    )

    try:
        await create_table(pool)
        await insert_students(pool)
        students = await fetch_students(pool)
        print("\nСписок студентов:")
        for s in students:
            print(f"ID: {s['id']}, Имя: {s['name']}, Возраст: {s['age']}")

    finally:
        await pool.close()
        print("\nПул соединений закрыт.")
