
import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order



@pytest.fixture
def prepared_orders():
    return [
        {'id': 101, 'user': 'alice', 'amount': 100.0, 'status': 'completed'},
        {'id': 202, 'user': 'bob', 'amount': 200.5, 'status': 'pending'},
        {'id': 303, 'user': 'alice', 'amount': 50, 'status': 'completed'},
        {'id': 404, 'user': 'charlie', 'amount': 300, 'status': 'cancelled'},
    ]


def test_filter_returns_completed(prepared_orders):
    completed = filter_orders(prepared_orders, 'completed')
    assert isinstance(completed, list)
    assert len(completed) == 2
    for o in completed:
        assert o['status'] == 'completed'

def test_filter_invalid_status_type_raises(prepared_orders):
    with pytest.raises(TypeError):
        filter_orders(prepared_orders, None)


def test_count_orders_grouping(prepared_orders):
    user_counts = count_orders_by_user(prepared_orders)
    assert isinstance(user_counts, dict)
    assert user_counts['alice'] == 2
    assert user_counts['bob'] == 1
    assert user_counts['charlie'] == 1

def test_count_orders_empty_input():
    result = count_orders_by_user([])
    assert result == {}
    assert len(result) == 0


def test_total_revenue_correct_sum(prepared_orders):
    total = calculate_total_revenue(prepared_orders)
    expected_sum = 100.0 + 200.5 + 50 + 300
    assert round(total, 2) == round(expected_sum, 2)

def test_total_revenue_empty_list_returns_zero():
    empty_revenue = calculate_total_revenue([])
    assert empty_revenue == 0

def test_total_revenue_negative_amount_causes_error():
    bad_data = [
        {'id': 555, 'user': 'john', 'amount': -20, 'status': 'completed'}
    ]
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        calculate_total_revenue(bad_data)

def test_validate_proper_order():
    valid_data = {'id': 999, 'user': 'mike', 'amount': 123.45, 'status': 'completed'}
    assert validate_order(valid_data) is True

def test_validate_fails_on_missing_keys():
    incomplete_data = {'id': 888, 'user': 'tom', 'amount': 42}
    with pytest.raises(ValueError, match="Order missing required fields."):
        validate_order(incomplete_data)

def test_validate_fails_on_negative_amount():
    order_with_issue = {'id': 777, 'user': 'lisa', 'amount': -99, 'status': 'pending'}
    with pytest.raises(ValueError, match="Amount must be non-negative number."):
        validate_order(order_with_issue)

def test_validate_fails_on_wrong_user_type():
    order_wrong_user = {'id': 666, 'user': 123456, 'amount': 10, 'status': 'cancelled'}
    with pytest.raises(TypeError, match="User must be a string."):
        validate_order(order_wrong_user)

def test_validate_fails_when_not_dict():
    with pytest.raises(TypeError, match="Order must be a dictionary."):
        validate_order(12345)
