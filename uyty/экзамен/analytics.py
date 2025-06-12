def filter_orders(orders, status):
    if not isinstance(status, str):
        raise TypeError("Status must be a string")
    return [order for order in orders if order.get("status") == status]

def calculate_total_revenue(orders):
    total = 0
    for order in orders:
        amount = order.get("amount", 0)
        if amount < 0:
            raise ValueError("Order amount cannot be negative")
        total += amount
    return total

def count_orders_by_user(orders):
    user_counts = {}
    for order in orders:
        user = order.get("user")
        if user:
            user_counts[user] = user_counts.get(user, 0) + 1
    return user_counts

def validate_order(order):
    required_fields = ["id", "user", "amount", "status"]
    for field in required_fields:
        if field not in order:
            raise ValueError(f"Missing required field: {field}")
    
    if not isinstance(order["user"], str):
        raise TypeError("User must be a string")
    
    if not isinstance(order["amount"], (int, float)) or order["amount"] <= 0:
        raise ValueError("Amount must be a positive number")
    
    return True