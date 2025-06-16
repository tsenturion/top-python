import pytest
from analytics import validate_order, filter_orders, calculate_total_revenue, count_orders_by_user

#Фикстуры
@pytest.fixture
def orders():
    return [
        {"id": 1, "user": "Alice", "amount": 100.50, "status": "completed"},
        {"id": 2, "user": "Bob", "amount": 200.75, "status": "pending"},
        {"id": 3, "user": "Alice", "amount": 50.25, "status": "completed"},
        {"id": 4, "user": "Charlie", "amount": 300.00, "status": "shipped"},
    ]

#Тесты функции validate_order
def test_validate_order_correct():
    order = {"id": 1, "user": "Alice", "amount": 100.50, "status": "completed"}
    assert validate_order(order) is True

def test_validate_order_not_dict():
    with pytest.raises(TypeError):
        validate_order("not a dict")

def test_validate_order_missing_fields():
    with pytest.raises(ValueError):
        validate_order({"id": 1, "user": "Alice"})

def test_validate_order_invalid_amount():
    with pytest.raises(ValueError):
        validate_order({"id": 1, "user": "Alice", "amount": -100, "status": "completed"})

def test_validate_order_invalid_user_type():
    with pytest.raises(TypeError):
        validate_order({"id": 1, "user": 123, "amount": 100.50, "status": "completed"})

#Тесты функции filter_orders
def test_filter_orders_correct(orders):
    filtered = filter_orders(orders, "completed")
    assert len(filtered) == 2
    assert all(order["status"] == "completed" for order in filtered)

def test_filter_orders_empty_result(orders):
    assert filter_orders(orders, "cancelled") == []

def test_filter_orders_invalid_status_type():
    with pytest.raises(TypeError):
        filter_orders([], 123)  

# Тесты функции calculate_total_revenue 
def test_calculate_total_revenue_correct(orders):
    assert calculate_total_revenue(orders) == 651.50

def test_calculate_total_revenue_empty_list():
    assert calculate_total_revenue([]) == 0

def test_calculate_total_revenue_invalid_order():
    with pytest.raises(ValueError):
        calculate_total_revenue([{"id": 1, "user": "Alice", "amount": -100, "status": "completed"}])

#Тесты функции count_orders_by_user
def test_count_orders_by_user_correct(orders):
    result = count_orders_by_user(orders)
    assert result == {"Alice": 2, "Bob": 1, "Charlie": 1}

def test_count_orders_by_user_empty_list():
    assert count_orders_by_user([]) == {}

def test_count_orders_by_user_invalid_order():
    with pytest.raises(ValueError):
        count_orders_by_user([{"id": 1, "user": "Alice"}])