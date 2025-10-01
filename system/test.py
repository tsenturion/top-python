import asyncio
import asyncpg

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


if __name__ == "__main__":
    asyncio.run(main())
