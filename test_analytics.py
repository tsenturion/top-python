import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order

@pytest.fixture
def sample_orders():
    return [
        {'id': 1, 'user': 'alice', 'amount': 100.0, 'status': 'completed'},
        {'id': 2, 'user': 'bob', 'amount': 200.5, 'status': 'pending'},
        {'id': 3, 'user': 'alice', 'amount': 50, 'status': 'completed'},
        {'id': 4, 'user': 'charlie', 'amount': 300, 'status': 'cancelled'},
    ]

def test_filter_orders_valid(sample_orders):
    result = filter_orders(sample_orders, 'completed')
    assert isinstance(result, list)
    assert len(result) == 2
    for order in result:
        assert order['status'] == 'completed'

def test_filter_orders_invalid_status_type(sample_orders):
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123) 


def test_calculate_total_revenue_valid(sample_orders):
    result = calculate_total_revenue(sample_orders)
    expected_total = 100.0 + 200.5 + 50 + 300
    assert isinstance(result, float)
    assert result == round(expected_total, 2)

def test_calculate_total_revenue_empty():
    assert calculate_total_revenue([]) == 0

def test_calculate_total_revenue_invalid_amount():
    orders = [
        {'id': 1, 'user': 'alice', 'amount': -10, 'status': 'completed'}, 
    ]
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        calculate_total_revenue(orders)

def test_count_orders_by_user_valid(sample_orders):
    result = count_orders_by_user(sample_orders)
    assert isinstance(result, dict)
    assert result == {
        'alice': 2,
        'bob': 1,
        'charlie': 1
    }

def test_count_orders_by_user_empty():
    result = count_orders_by_user([])
    assert result == {}

def test_validate_order_valid():
    order = {'id': 1, 'user': 'alice', 'amount': 100, 'status': 'completed'}
    assert validate_order(order) is True

def test_validate_order_missing_fields():
    order = {'id': 1, 'user': 'alice', 'amount': 100}  
    with pytest.raises(ValueError, match="Order missing required fields."):
        validate_order(order)

def test_validate_order_invalid_amount():
    order = {'id': 1, 'user': 'alice', 'amount': -5, 'status': 'completed'}
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        validate_order(order)

def test_validate_order_invalid_user_type():
    order = {'id': 1, 'user': 123, 'amount': 50, 'status': 'completed'}
    with pytest.raises(TypeError, match="User must be a string."):
        validate_order(order)

def test_validate_order_invalid_order_type():
    with pytest.raises(TypeError, match="Order must be a dictionary."):
        validate_order("not a dict")

def test_filter_orders_no_match(sample_orders):
    result = filter_orders(sample_orders, 'nonexistent_status')
    assert result == []

def test_filter_orders_empty_list():
    result = filter_orders([], 'completed')
    assert result == []

def test_calculate_total_revenue_zero_amount():
    orders = [
        {'id': 1, 'user': 'alice', 'amount': 0, 'status': 'completed'},
        {'id': 2, 'user': 'bob', 'amount': 0, 'status': 'pending'},
    ]
    result = calculate_total_revenue(orders)
    assert result == 0

def test_calculate_total_revenue_rounding():
    orders = [
        {'id': 1, 'user': 'alice', 'amount': 1.005, 'status': 'completed'},
        {'id': 2, 'user': 'bob', 'amount': 2.335, 'status': 'completed'},
    ]
    result = calculate_total_revenue(orders)
    assert result == round(1.005 + 2.335, 2)

def test_count_orders_by_user_case_sensitive():
    orders = [
        {'id': 1, 'user': 'Alice', 'amount': 50, 'status': 'completed'},
        {'id': 2, 'user': 'alice', 'amount': 70, 'status': 'completed'},
    ]
    result = count_orders_by_user(orders)
    assert result == {'Alice': 1, 'alice': 1}

def test_count_orders_by_user_single_user():
    orders = [
        {'id': 1, 'user': 'bob', 'amount': 50, 'status': 'completed'},
        {'id': 2, 'user': 'bob', 'amount': 150, 'status': 'pending'},
    ]
    result = count_orders_by_user(orders)
    assert result == {'bob': 2}

def test_validate_order_zero_amount():
    order = {'id': 1, 'user': 'alice', 'amount': 0, 'status': 'completed'}
    assert validate_order(order) is True

def test_validate_order_empty_user():
    order = {'id': 1, 'user': '', 'amount': 100, 'status': 'completed'}
    assert validate_order(order) is True

def test_validate_order_invalid_amount_type():
    order = {'id': 1, 'user': 'alice', 'amount': '100', 'status': 'completed'}
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        validate_order(order)
