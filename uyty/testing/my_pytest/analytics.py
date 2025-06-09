def validate_order(order):
    required_keys = {'id', 'user', 'amount', 'status'}
    if not isinstance(order, dict):
        raise TypeError("Order must be a dictionary.")
    if not required_keys.issubset(order):
        raise ValueError("Order missing required fields.")
    if not isinstance(order['amount'], (int, float)) or order['amount'] < 0:
        raise ValueError("Amount must be non-negative number.")
    if not isinstance(order['user'], str):
        raise TypeError("User must be a string.")
    return True

def filter_orders(orders, status):
    if not isinstance(status, str):
        raise TypeError("Status must be a string.")
    return [order for order in orders if order.get('status') == status]

def calculate_total_revenue(orders):
    total = 0
    for order in orders:
        validate_order(order)
        total += order['amount']
    return round(total, 2)

def count_orders_by_user(orders):
    result = {}
    for order in orders:
        validate_order(order)
        user = order['user']
        result[user] = result.get(user, 0) + 1
    return result
