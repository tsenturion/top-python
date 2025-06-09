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
        {'id': 1, 'user': 'alice', 'amount': 150.0, 'status': 'delivered'},
        {'id': 2, 'user': 'bob', 'amount': 200, 'status': 'pending'},
        {'id': 3, 'user': 'alice', 'amount': 100, 'status': 'delivered'},
        {'id': 4, 'user': 'charlie', 'amount': 50, 'status': 'canceled'},
    ]
def test_filter_orders_correct(sample_orders):
    filtered = filter_orders(sample_orders, 'delivered')
    assert isinstance(filtered, list)
    assert all(order['status'] == 'delivered' for order in filtered)
    assert {order['id'] for order in filtered} == {1, 3}
def test_filter_orders_incorrect_status_type(sample_orders):
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123)
def test_calculate_total_revenue_ok(sample_orders):
    total = calculate_total_revenue(sample_orders)
    assert isinstance(total, float)
    assert total == 500.0  
def test_calculate_total_revenue_empty():
    assert calculate_total_revenue([]) == 0.0
def test_calculate_total_revenue_invalid_order_negative_amount():
    orders = [
        {'id': 1, 'user': 'bob', 'amount': -100, 'status': 'pending'}
    ]
    with pytest.raises(ValueError):
        calculate_total_revenue(orders)
def test_calculate_total_revenue_invalid_order_missing_field():
    orders = [
        {'user': 'bob', 'amount': 100, 'status': 'pending'} 
    ]
    with pytest.raises(ValueError):
        calculate_total_revenue(orders)
def test_count_orders_by_user_normal(sample_orders):
    result = count_orders_by_user(sample_orders)
    assert isinstance(result, dict)
    assert result == {'alice': 2, 'bob': 1, 'charlie': 1}
def test_count_orders_by_user_empty():
    assert count_orders_by_user([]) == {}
def test_count_orders_by_user_invalid_user_type():
    orders = [
        {'id': 1, 'user': 123, 'amount': 100, 'status': 'pending'}
    ]
    with pytest.raises(TypeError):
        count_orders_by_user(orders)
def test_count_orders_by_user_missing_required_field():
    orders = [
        {'id': 1, 'amount': 100, 'status': 'pending'} 
    ]
    with pytest.raises(ValueError):
        count_orders_by_user(orders)
def test_validate_order_valid():
    order = {'id': 5, 'user': 'dave', 'amount': 100, 'status': 'pending'}
    assert validate_order(order) is True
def test_validate_order_missing_required_fields():
    order = {'id': 5, 'user': 'dave', 'amount': 100}
    with pytest.raises(ValueError):
        validate_order(order)
    order2 = {'user': 'dave', 'amount': 100, 'status': 'pending'}
    with pytest.raises(ValueError):
        validate_order(order2)
def test_validate_order_wrong_types():
    order = {'id': 1, 'user': 123, 'amount': 100, 'status': 'pending'}
    with pytest.raises(TypeError):
        validate_order(order)
    order2 = {'id': 1, 'user': 'kate', 'amount': "сто", 'status': 'pending'}
    with pytest.raises(ValueError):
        validate_order(order2)
def test_validate_order_negative_amount():
    order = {'id': 1, 'user': 'kate', 'amount': -50, 'status': 'delivered'}
    with pytest.raises(ValueError):
        validate_order(order)
def test_validate_order_not_dict():
    order = ['id', 'user', 'amount', 'status']
    with pytest.raises(TypeError):
        validate_order(order)
