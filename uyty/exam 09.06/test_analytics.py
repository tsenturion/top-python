import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order

@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "user": "Alice", "amount": 100, "status": "completed"},
        {"id": 2, "user": "Bob", "amount": 200, "status": "pending"},
        {"id": 3, "user": "Alice", "amount": 50, "status": "completed"},
        {"id": 4, "user": "Charlie", "amount": 300, "status": "canceled"},
        {"id": 5, "user": "Bob", "amount": 150, "status": "completed"},
    ]


def test_filter_orders_by_status(sample_orders, capsys):
    print("\nТестирование по статусу")
    filtered = filter_orders(sample_orders, "completed")
    print(f"Найдено заказов: {len(filtered)}")
    print("ЗАказы:", filtered)
    assert len(filtered) == 3
    assert all(order["status"] == "completed" for order in filtered)
    print("Фильтрация по статусу работает")
    
    with capsys.disabled():
        print("\nResult:")
        for order in filtered:
            print(f"ID: {order['id']}, User: {order['user']}, Amount: {order['amount']}")

def test_filter_orders_empty_result(sample_orders):
    print("\nТестрирование филтрации с пустым значением")
    filtered = filter_orders(sample_orders, "shipped")
    print(f"Найдено заказов: {len(filtered)} (should be - 0)")
    assert len(filtered) == 0
    print("Фильтр вернёт пустое знаение если нет сходства")

def test_filter_orders_invalid_status_type(sample_orders):
    print("\nТестирование неверного статуса")
    try:
        filter_orders(sample_orders, 123)
        print("Не пройдено, нет исключений")
        assert False
    except TypeError as e:
        print(f"Исключение: {type(e).__name__}: {e}")
        assert True


def test_calculate_total_revenue(sample_orders):
    print("\nТестрирование количество выручки")
    total = calculate_total_revenue(sample_orders)
    expected = 100 + 200 + 50 + 300 + 150
    print(f"Выручка: {total} (ожидается - {expected})")
    assert total == expected
    print("Сумма верна")

def test_calculate_total_revenue_empty_list():
    print("\nТест пустой выручки")
    total = calculate_total_revenue([])
    print(f"Выручка: {total} (ожидается - 0)")
    assert total == 0
    print("Для каждого списка возвращается 0")

def test_calculate_total_revenue_negative_amount():
    print("\nТестирование отрицательной суммы")
    try:
        calculate_total_revenue([{"user": "Alice", "amount": -100, "status": "completed"}])
        print("Тест не пройден, нет исключений")
        assert False
    except ValueError as e:
        print(f"Вызванно исключение: {type(e).__name__}: {e}")
        assert True

def test_count_orders_by_user(sample_orders):
    print("\nЗаказы пользователей")
    counts = count_orders_by_user(sample_orders)
    expected = {"Alice": 2, "Bob": 2, "Charlie": 1}
    print("Результат:", counts)
    print("Ожидаемо:", expected)
    assert counts == expected
    print("Счёт верен")

def test_count_orders_by_user_empty_list():
    print("\nСчёт пустых значений")
    counts = count_orders_by_user([])
    print("Результат:", counts)
    assert counts == {}
    print("За пустой список возвращается пустой словарь")
#I'm gonna put Yipeee here, noone will see this anyway so
#Yipeeee!
def test_validate_order_valid():
    print("\nТест на правильный заказ")
    order = {"id": 1, "user": "Alice", "amount": 100, "status": "completed"}
    result = validate_order(order)
    print("Заказ:", order)
    assert result is True
    print("Правильный заказ найден верно")

def test_validate_order_missing_field():
    print("\nТест на проверку на пустого значения заказа")
    order = {"id": 1, "user": "Alice", "status": "completed"}
    try:
        validate_order(order)
        print("Тест не пройден, нет исключений")
        assert False
    except ValueError as e:
        print(f"Исключение: {type(e).__name__}: {e}")
        assert True

def test_validate_order_invalid_user_type():
    print("\nТест на проверку заказов с неверными пользователями")
    order = {"id": 1, "user": 123, "amount": 100, "status": "completed"}
    try:
        validate_order(order)
        print("Не пройден, нет исключений")
        assert False
    except TypeError as e:
        print(f"Исключение: {type(e).__name__}: {e}")
        assert True


def test_validate_order_negative_amount():
    print("\nТест на проверку отрицательных значений")
    order = {"id": 1, "user": "Alice", "amount": -100, "status": "completed"}
    try:
        validate_order(order)
        print("Не пройден, нет исключений")
        assert False
    except ValueError as e:
        print(f"Исключение: {type(e).__name__}: {e}")
        assert True


if __name__ == "__main__":
    pytest.main(["-v", "--capture=no"])