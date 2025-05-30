# абстрактные продукты - интерфейс/ABC cls, определяют общее поведение объектов
# интерфейсы работы с базой

from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def create_user(self, name: str, email: str):
        pass

# конкретные продукты - реализуют абстрактные продукты
import mysql.connector

class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("подключение к mysql")
        return mysql.connector.connect(host='localhost', user='root', password='1234', database='users_db')

class MySQLUserRepository(UserRepository):
    def __init__(self, connection):
        self.connection = connection

    def get_user(self, user_id: int):
        print(f"получаем пользователя с {user_id} из MySQL")
        return {"id": user_id, "name": "иван", "email": "ivan@example.com"}

    def create_user(self, name: str, email: str):
        print(f"создание пользователя {name} в MySQL")

import psycopg2

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("подключение к PosgtreSQL")
        return psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='users_db')


class PostgreSQLUserRepository(UserRepository):
    def __init__(self, connection):
        self.connection = connection

    def get_user(self, user_id: int):
        print(f"получаем пользователя с {user_id} из PostgreSQL")
        return {"id": user_id, "name": "иван", "email": "ivan@example.com"}

    def create_user(self, name: str, email: str):
        print(f"создание пользователя {name} в PostgreSQL")

# абстрактная фабрика - интерфейс/ABC cls, набор методов для создания объектов
class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass

    @abstractmethod
    def create_user_repository(self, connection: DatabaseConnection) -> UserRepository:
        pass

# конкретные фабрики - реализуют абстрактную фабрику
class MySQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

    def create_user_repository(self, connection: DatabaseConnection) -> UserRepository:
        return MySQLUserRepository(connection)


class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

    def create_user_repository(self, connection: DatabaseConnection) -> UserRepository:
        return MySQLUserRepository(connection)

# клиентский код - использует фабрику, работает с интерфейсами

def main(factory: DatabaseFactory):
    connection = factory.create_connection()
    conn_instance = connection.connect()
    user_repo = factory.create_user_repository(connection)
    user_repo.create_user("Петр", "petr@example.com")
    user = user_repo.get_user(1)
    print(user)

db_type = "PostgreSQL"

if db_type == 'PostgreSQL':
    factory = PostgreSQLFactory()
else:
    factory = MySQLFactory()

main(factory)
