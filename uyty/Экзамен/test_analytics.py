import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order

@pytest.fixture
def sample_orders():
    return [
        {'user': 'alice', 'status': 'completed', 'amount': 100.0},
        {'user': 'bob', 'status': 'pending', 'amount': 200.5},
        {'user': 'alice', 'status': 'completed', 'amount': 150.0},
        {'user': 'carol', 'status': 'cancelled', 'amount': 50.0},
    ]
    
def test_filter_orders_valid(sample_orders):
    filtered = filter_orders(sample_orders, 'completed')
    assert isinstance(filtered, list)
    assert len(filtered) == 2
    assert all(order['status'] == 'completed' for order in filtered)

def test_filter_orders_invalid_status_type(sample_orders):
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123)  

def test_calculate_total_revenue_correct(sample_orders):
    total = calculate_total_revenue(sample_orders)
    expected = 100.0 + 200.5 + 150.0 + 50.0
    assert total == expected
    assert isinstance(total, float)

def test_calculate_total_revenue_empty():
    assert calculate_total_revenue([]) == 0.0

def test_calculate_total_revenue_negative_amount():
    orders = [{'user': 'dave', 'status': 'completed', 'amount': -100.0}]
    with pytest.raises(ValueError):
        calculate_total_revenue(orders)

def test_count_orders_by_user_valid(sample_orders):
    result = count_orders_by_user(sample_orders)
    assert isinstance(result, dict)
    assert result['alice'] == 2
    assert result['bob'] == 1
    assert result['carol'] == 1

def test_count_orders_by_user_empty():
    assert count_orders_by_user([]) == {}

def test_validate_order_valid():
    order = {'user': 'alice', 'status': 'completed', 'amount': 100.0}
    assert validate_order(order) is True

def test_validate_order_missing_field():
    order = {'user': 'bob', 'amount': 50.0}  # нет 'status'
    with pytest.raises(KeyError):
        validate_order(order)

def test_validate_order_invalid_user_type():
    order = {'user': 123, 'status': 'completed', 'amount': 50.0}
    with pytest.raises(TypeError):
        validate_order(order)

def test_validate_order_invalid_amount_type():
    order = {'user': 'dave', 'status': 'pending', 'amount': 'a lot'}
    with pytest.raises(TypeError):
        validate_order(order)

def test_validate_order_negative_amount():
    order = {'user': 'eve', 'status': 'completed', 'amount': -10.0}
    with pytest.raises(ValueError):
        validate_order(order)
