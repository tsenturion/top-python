from my_pytest.example import reverse


def test_reverse():
    assert reverse("Src") == "crS"

def test_reverse_for_empty_string():
    assert reverse("") == ""

def test_reverse_for_None():
    assert reverse(None) == None

def test_stack_is_empty():
    stack = []
    assert not stack

def test_stack_append():
    stack = []
    stack.append(1)
    assert bool(stack)

def test_stack_pop():
    stack = [1]
    stack.pop()
    assert not stack

import time
import pytest

"""
фикстуры
Функциональная область видимости (function): Фикстура будет выполнена для каждой тестовой функции, в которой она используется. Это область видимости по умолчанию.
Классовая область видимости (class): Фикстура будет выполнена для каждого метода в классе, в котором она используется.
Модульная область видимости (module): Фикстура будет выполнена один раз для каждого модуля, в котором она используется.
Сессионная область видимости (session): Фикстура будет выполнена один раз для всей тестовой сессии.
Пакетная область видимости (package): Фикстура будет выполнена один раз для каждого пакета, в котором она используется.
"""
@pytest.fixture
def now():
    return int(time.time() * 1000)

def test_first_example_text(now):
    print(now)

def test_second_example_text(now):
    print(now)

@pytest.fixture
def coll():
    return [1, 2, 3, 4]

def test_first_example(coll):
    coll.append(5)
    assert coll == [1, 2, 3, 4, 5]

def test_second_example(coll):
    coll.pop()
    assert coll == [1, 2, 3]

@pytest.fixture
def users():
    return [{"name": "user1"}, {"name": "user2"}]

@pytest.fixture
def admin():
    return [{"name": "admin"}]

@pytest.fixture
def all_users(users, admin):
    return users + admin

def test_example(all_users, admin):
    expected_admins = get_admins(all_users)
    assert expected_admins == admin

def get_admins(users):
    return [user for user in users if user["name"] == "admin"]

@pytest.fixture
def coll1():
    return [1, 2, 3, 4]

@pytest.fixture(autouse=True)
def setup_coll1(coll1):
    coll1[0] = "a"

def test_example1(coll1):
    assert coll1 == ["a", 2, 3, 4]

def test_example2(coll1):
    assert coll1[0] == "a"

@pytest.fixture(scope="session")
def db():
    ...

@pytest.fixture
def user():
    return {"id": 1, "name": "user1"}

def test_db(db, user):
    save_to_db(db, user)
    expected_user = get_from_db(db, id=1)
    assert expected_user == user