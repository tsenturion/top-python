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
        {"id": 1, "user": "Alice", "status": "completed", "amount": 100},
        {"id": 2, "user": "Bob", "status": "pending", "amount": 200},
        {"id": 3, "user": "Alice", "status": "completed", "amount": 150},
        {"id": 4, "user": "Charlie", "status": "cancelled", "amount": 50},
    ]

@pytest.fixture
def empty_orders():
    return []
    
def test_filter_orders_by_status(sample_orders):
    filtered = filter_orders(sample_orders, "completed")
    assert len(filtered) == 2
    assert all(order["status"] == "completed" for order in filtered)
    
def test_filter_orders_empty_result(sample_orders):
    filtered = filter_orders(sample_orders, "shipped")
    assert len(filtered) == 0
    assert isinstance(filtered, list)
    
def test_filter_orders_invalid_status_type(sample_orders):
    with pytest.raises(TypeError):
        filter_orders(sample_orders, 123)
        
def test_calculate_total_revenue(sample_orders):
    assert calculate_total_revenue(sample_orders) == 500
    
def test_calculate_total_revenue_empty_list(empty_orders):
    assert calculate_total_revenue(empty_orders) == 0
    
def test_calculate_total_revenue_negative_amount():
    with pytest.raises(ValueError):
        calculate_total_revenue([{"id": 1, "user": "Alice", "amount": -100, "status": "completed"}])
        
def test_count_orders_by_user(sample_orders):
    counts = count_orders_by_user(sample_orders)
    assert counts == {"Alice": 2, "Bob": 1, "Charlie": 1}
    
def test_count_orders_by_user_empty_list(empty_orders):
    assert count_orders_by_user(empty_orders) == {}
    
def test_validate_order_correct():
    order = {"id": 1, "user": "Alice", "status": "completed", "amount": 100}
    assert validate_order(order) is True
    
def test_validate_order_missing_field():
    with pytest.raises(ValueError):
        validate_order({"user": "Alice", "amount": 100, "status": "completed"})
        
def test_validate_order_invalid_user_type():
    with pytest.raises(TypeError):
        validate_order({"id": 1, "user": 123, "status": "completed", "amount": 100})
        
def test_validate_order_invalid_amount_value():
    with pytest.raises(ValueError):
        validate_order({"id": 1, "user": "Alice", "status": "completed", "amount": -100})


