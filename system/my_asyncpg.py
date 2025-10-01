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

asyncio.run(main())