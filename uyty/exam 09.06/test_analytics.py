import pytest
from analytics import filter_orders, calculate_total_revenue, count_orders_by_user, validate_order

# fixture with examples 
@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "user": "Alice", "amount": 100, "status": "completed"},
        {"id": 2, "user": "Bob", "amount": 200, "status": "pending"},
        {"id": 3, "user": "Alice", "amount": 50, "status": "completed"},
        {"id": 4, "user": "Charlie", "amount": 300, "status": "canceled"},
        {"id": 5, "user": "Bob", "amount": 150, "status": "completed"},
    ]


def test_filter_orders_by_status(sample_orders, capsys):
    print("\nTesting orders by ststus")
    filtered = filter_orders(sample_orders, "completed")
    print(f"Orders found: {len(filtered)}")
    print("Orders:", filtered)
    assert len(filtered) == 3
    assert all(order["status"] == "completed" for order in filtered)
    print("Status filtration works fine")
    
    with capsys.disabled():
        print("\nResult:")
        for order in filtered:
            print(f"ID: {order['id']}, User: {order['user']}, Amount: {order['amount']}")

def test_filter_orders_empty_result(sample_orders):
    print("\nTesting filtration with empty value")
    filtered = filter_orders(sample_orders, "shipped")
    print(f"Orders found: {len(filtered)} (should be - 0)")
    assert len(filtered) == 0
    print("Filter returns empty value if there is no equals")

def test_filter_orders_invalid_status_type(sample_orders):
    print("\nTest for wrong status")
    try:
        filter_orders(sample_orders, 123)
        print("Not passed: no exceptions")
        assert False
    except TypeError as e:
        print(f"Exception: {type(e).__name__}: {e}")
        assert True


def test_calculate_total_revenue(sample_orders):
    print("\nTesting amount of revenue")
    total = calculate_total_revenue(sample_orders)
    expected = 100 + 200 + 50 + 300 + 150
    print(f"Revenue: {total} (expected - {expected})")
    assert total == expected
    print("Sum is correct")

def test_calculate_total_revenue_empty_list():
    print("\nTest for empty revenue")
    total = calculate_total_revenue([])
    print(f"Revenue: {total} (expected - 0)")
    assert total == 0
    print("For each list returns 0")

def test_calculate_total_revenue_negative_amount():
    print("\nTesting negative sum")
    try:
        calculate_total_revenue([{"user": "Alice", "amount": -100, "status": "completed"}])
        print("test is not passed: no exception")
        assert False
    except ValueError as e:
        print(f"Exception called: {type(e).__name__}: {e}")
        assert True

def test_count_orders_by_user(sample_orders):
    print("\nOrders by users")
    counts = count_orders_by_user(sample_orders)
    expected = {"Alice": 2, "Bob": 2, "Charlie": 1}
    print("Result:", counts)
    print("Expected:", expected)
    assert counts == expected
    print("count is correct")

def test_count_orders_by_user_empty_list():
    print("\nCount for empty values")
    counts = count_orders_by_user([])
    print("Result:", counts)
    assert counts == {}
    print("For empty list empty dict is returned")
#I'm gonna put Yipeee here, noone will see this anyway so
#Yipeeee!
def test_validate_order_valid():
    print("\nTest for correct order")
    order = {"id": 1, "user": "Alice", "amount": 100, "status": "completed"}
    result = validate_order(order)
    print("Order:", order)
    assert result is True
    print("Valid order is found correctly")

def test_validate_order_missing_field():
    print("\nTest on order validation with empty field")
    order = {"id": 1, "user": "Alice", "status": "completed"}
    try:
        validate_order(order)
        print("Not passed: no exception")
        assert False
    except ValueError as e:
        print(f"Exception: {type(e).__name__}: {e}")
        assert True

def test_validate_order_invalid_user_type():
    print("\nTest for validate order with invalid user")
    order = {"id": 1, "user": 123, "amount": 100, "status": "completed"}
    try:
        validate_order(order)
        print("Not passed: no exception")
        assert False
    except TypeError as e:
        print(f"Exception: {type(e).__name__}: {e}")
        assert True


def test_validate_order_negative_amount():
    print("\nTest for validation of order with negative value")
    order = {"id": 1, "user": "Alice", "amount": -100, "status": "completed"}
    try:
        validate_order(order)
        print("Not passed: not exception")
        assert False
    except ValueError as e:
        print(f"Exception: {type(e).__name__}: {e}")
        assert True


if __name__ == "__main__":
    pytest.main(["-v", "--capture=no"])