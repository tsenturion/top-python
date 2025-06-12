# test_analytics.py

import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order

# ---- Данные для тестирования ----

@pytest.fixture
def orders_sample():
    return [
        {'id': 1, 'user': 'alice', 'amount': 100.0, 'status': 'completed'},
        {'id': 2, 'user': 'bob', 'amount': 200.5, 'status': 'pending'},
        {'id': 3, 'user': 'alice', 'amount': 50, 'status': 'completed'},
        {'id': 4, 'user': 'charlie', 'amount': 300, 'status': 'cancelled'},
    ]

# ---- Тесты функции calculate_total_revenue ----

def test_revenue_on_empty_list():
    assert calculate_total_revenue([]) == 0

def test_revenue_on_valid_orders(orders_sample):
    revenue = calculate_total_revenue(orders_sample)
    assert isinstance(revenue, float)
    expected = round(100.0 + 200.5 + 50 + 300, 2)
    assert revenue == expected

def test_revenue_negative_amount_error():
    faulty_orders = [
        {'id': 1, 'user': 'alice', 'amount': -10, 'status': 'completed'},
    ]
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        calculate_total_revenue(faulty_orders)

# ---- Тесты функции validate_order ----

def test_valid_order_validation():
    order_data = {'id': 1, 'user': 'alice', 'amount': 100, 'status': 'completed'}
    assert validate_order(order_data) == True

def test_missing_fields_in_order():
    incomplete_order = {'id': 1, 'user': 'alice', 'amount': 100}  # нет status
    with pytest.raises(ValueError, match="Order missing required fields."):
        validate_order(incomplete_order)

def test_invalid_amount_in_order():
    bad_order = {'id': 1, 'user': 'alice', 'amount': -5, 'status': 'completed'}
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        validate_order(bad_order)

def test_user_type_is_not_string():
    wrong_user = {'id': 1, 'user': 999, 'amount': 50, 'status': 'completed'}
    with pytest.raises(TypeError, match="User must be a string."):
        validate_order(wrong_user)

def test_input_not_a_dict():
    with pytest.raises(TypeError, match="Order must be a dictionary."):
        validate_order("string_instead_of_dict")

# ---- Тесты функции count_orders_by_user ----

def test_user_order_count(orders_sample):
    result = count_orders_by_user(orders_sample)
    assert isinstance(result, dict)
    expected = {
        'alice': 2,
        'bob': 1,
        'charlie': 1
    }
    assert result == expected

def test_user_order_count_empty_list():
    result = count_orders_by_user([])
    assert result == {}
    assert len(result) == 0

# ---- Тесты функции filter_orders ----

def test_filter_completed_orders(orders_sample):
    filtered = filter_orders(orders_sample, 'completed')
    assert type(filtered) is list
    assert len(filtered) == 2
    for item in filtered:
        assert item['status'] == 'completed'

def test_filter_invalid_status_type(orders_sample):
    with pytest.raises(TypeError):
        filter_orders(orders_sample, 42)  # статус передан как число