import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order

@pytest.fixture
def sample_orders():
    return [
        {'id': 1, 'user': 'alice', 'amount': 100.0, 'status': 'shipped'},
        {'id': 2, 'user': 'bob', 'amount': 150.5, 'status': 'pending'},
        {'id': 3, 'user': 'alice', 'amount': 200, 'status': 'shipped'},
        {'id': 4, 'user': 'charlie', 'amount': 0, 'status': 'cancelled'},
    ]

# 1. filter_orders tests
def test_filter_orders_correct_result(sample_orders):
    shipped_orders = filter_orders(sample_orders, 'shipped')
    assert isinstance(shipped_orders, list)
    assert all(order['status'] == 'shipped' for order in shipped_orders)
    assert len(shipped_orders) == 2

def test_filter_orders_no_matches(sample_orders):
    result = filter_orders(sample_orders, 'delivered')
    assert result == []

def test_filter_orders_invalid_status_type(sample_orders):
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123)

# 2. calculate_total_revenue tests
def test_calculate_total_revenue_correct(sample_orders):
    total = calculate_total_revenue(sample_orders)
    expected = 100.0 + 150.5 + 200 + 0
    assert isinstance(total, float)
    assert abs(total - expected) < 1e-6

def test_calculate_total_revenue_empty():
    assert calculate_total_revenue([]) == 0

def test_calculate_total_revenue_invalid_order_amount():
    orders = [{'id': 1, 'user': 'alice', 'amount': -10, 'status': 'shipped'}]
    with pytest.raises(ValueError):
        calculate_total_revenue(orders)

# 3. count_orders_by_user tests
def test_count_orders_by_user_correct(sample_orders):
    counts = count_orders_by_user(sample_orders)
    assert isinstance(counts, dict)
    assert counts.get('alice') == 2
    assert counts.get('bob') == 1
    assert counts.get('charlie') == 1

def test_count_orders_by_user_empty():
    assert count_orders_by_user([]) == {}

# 4. validate_order tests
def test_validate_order_valid():
    order = {'id': 1, 'user': 'dave', 'amount': 50, 'status': 'pending'}
    assert validate_order(order) is True

def test_validate_order_missing_fields():
    order = {'id': 1, 'user': 'dave', 'amount': 50}
    with pytest.raises(ValueError):
        validate_order(order)

def test_validate_order_invalid_user_type():
    order = {'id': 1, 'user': 123, 'amount': 50, 'status': 'pending'}
    with pytest.raises(TypeError):
        validate_order(order)

def test_validate_order_negative_amount():
    order = {'id': 1, 'user': 'dave', 'amount': -5, 'status': 'pending'}
    with pytest.raises(ValueError):
        validate_order(order)

def test_validate_order_not_dict():
    with pytest.raises(TypeError):
        validate_order(['not', 'a', 'dict'])