# test_analytics_pytest.py
import pytest
from analytics import (
    filter_orders,
    calculate_total_revenue,
    count_orders_by_user,
    validate_order
)

# Фикстура с тестовыми данными
@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "user": "Alice", "amount": 100, "status": "completed"},
        {"id": 2, "user": "Bob", "amount": 200, "status": "pending"},
        {"id": 3, "user": "Alice", "amount": 50, "status": "completed"},
        {"id": 4, "user": "Charlie", "amount": 300, "status": "cancelled"},
    ]

# Параметризованные тесты для filter_orders
@pytest.mark.parametrize("status,expected_count,expected_ids", [
    ("completed", 2, [1, 3]),
    ("pending", 1, [2]),
    ("cancelled", 1, [4]),
    ("shipped", 0, []),
])
def test_filter_orders(sample_orders, status, expected_count, expected_ids):
  
    result = filter_orders(sample_orders, status)
    assert len(result) == expected_count
    assert [order["id"] for order in result] == expected_ids

def test_filter_orders_invalid_status_type(sample_orders):
   
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123)

# Тесты для calculate_total_revenue
def test_calculate_total_revenue(sample_orders):
   
    assert calculate_total_revenue(sample_orders) == 650

def test_calculate_total_revenue_empty():
   
    assert calculate_total_revenue([]) == 0

@pytest.mark.parametrize("invalid_order", [
    {"amount": -100},
    {"amount": 0},
    {"amount": "100"},
])
def test_calculate_total_revenue_invalid(invalid_order):
  
    with pytest.raises(ValueError):
        calculate_total_revenue([invalid_order])

# Тесты для count_orders_by_user
def test_count_orders_by_user(sample_orders):
   
    result = count_orders_by_user(sample_orders)
    assert result == {"Alice": 2, "Bob": 1, "Charlie": 1}

def test_count_orders_by_user_empty():
    
    assert count_orders_by_user([]) == {}

# Параметризованные тесты для validate_order
@pytest.mark.parametrize("order,is_valid", [
    ({"id": 1, "user": "Alice", "amount": 100, "status": "completed"}, True),
    ({"id": 2, "user": "Bob", "amount": 200, "status": "pending"}, True),
    ({"user": "Alice", "amount": 100}, False),  # Нет id
    ({"id": 1, "user": 123, "amount": 100, "status": "completed"}, False),  # Неправильный тип user
    ({"id": 1, "user": "Alice", "amount": -100, "status": "completed"}, False),  # Отрицательная сумма
    ({"id": 1, "user": "Alice", "amount": "100", "status": "completed"}, False),  # Неправильный тип суммы
])
def test_validate_order(order, is_valid):
    
    if is_valid:
        assert validate_order(order) is True
    else:
        with pytest.raises((ValueError, TypeError)):
            validate_order(order)