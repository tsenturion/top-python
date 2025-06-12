import pytest
from analytics import (
    filter_orders,
    calculate_total_revenue,
    count_orders_by_user,
    validate_order,
)


@pytest.fixture
def sample_orders():
    return [
        {'id': 1, 'user': 'alice', 'amount': 100.0, 'status': 'paid'},
        {'id': 2, 'user': 'bob', 'amount': 50.5, 'status': 'pending'},
        {'id': 3, 'user': 'alice', 'amount': 25.75, 'status': 'paid'},
        {'id': 4, 'user': 'carol', 'amount': 0, 'status': 'cancelled'},
    ]

def test_filter_orders_correct(sample_orders):
    paid_orders = filter_orders(sample_orders, 'paid')
    assert isinstance(paid_orders, list)
    assert all(o['status'] == 'paid' for o in paid_orders)
    assert len(paid_orders) == 2

def test_filter_orders_no_matches(sample_orders):
    result = filter_orders(sample_orders, 'shipped')
    assert result == []

def test_filter_orders_invalid_status_type(sample_orders):
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123)

def test_calculate_total_revenue_correct(sample_orders):
    total = calculate_total_revenue(sample_orders)
    expected = sum(o['amount'] for o in sample_orders)
    assert isinstance(total, float)
    assert abs(total - expected) < 1e-6

def test_calculate_total_revenue_empty():
    assert calculate_total_revenue([]) == 0

def test_calculate_total_revenue_invalid_order_negative_amount():
    bad_orders = [{'id': 1, 'user': 'alice', 'amount': -10, 'status': 'paid'}]
    with pytest.raises(ValueError):
        calculate_total_revenue(bad_orders)

def test_count_orders_by_user_correct(sample_orders):
    counts = count_orders_by_user(sample_orders)
    assert isinstance(counts, dict)
    assert counts.get('alice') == 2
    assert counts.get('bob') == 1
    assert counts.get('carol') == 1

def test_count_orders_by_user_empty():
    assert count_orders_by_user([]) == {}

def test_count_orders_by_user_invalid_order():
    bad_orders = [{'id': 1, 'user': 123, 'amount': 10, 'status': 'paid'}]
    with pytest.raises(TypeError):
        count_orders_by_user(bad_orders)

def test_validate_order_valid():
    order = {'id': 10, 'user': 'john', 'amount': 20.5, 'status': 'paid'}
    assert validate_order(order) is True

def test_validate_order_missing_fields():
    order = {'id': 10, 'user': 'john', 'amount': 20.5}
    with pytest.raises(ValueError):
        validate_order(order)

def test_validate_order_invalid_amount_type():
    order = {'id': 10, 'user': 'john', 'amount': '20.5', 'status': 'paid'}
    with pytest.raises(ValueError):
        validate_order(order)

def test_validate_order_negative_amount():
    order = {'id': 10, 'user': 'john', 'amount': -1, 'status': 'paid'}
    with pytest.raises(ValueError):
        validate_order(order)

def test_validate_order_invalid_user_type():
    order = {'id': 10, 'user': 100, 'amount': 20, 'status': 'paid'}
    with pytest.raises(TypeError):
        validate_order(order)

def test_validate_order_not_dict():
    with pytest.raises(TypeError):
        validate_order(['not', 'a', 'dict'])
