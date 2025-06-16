def filter_orders(orders, status):
    if not isinstance(status, str):
        raise TypeError("Статус должен быть строкой.")
    return [order for order in orders if order.get('status') == status]
    
def calculate_total_revenue(orders):
    total = 0.0
    for order in orders:
        amount = order.get('amount')
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма заказа должна быть числом.")
        if amount < 0:
            raise ValueError("Сумма заказа не может быть отрицательной.")
        total += amount
    return total

def count_orders_by_user(orders):
    result = {}
    for order in orders:
        user = order.get('user')
        if user in result:
            result[user] += 1
        else:
            result[user] = 1
    return result

def validate_order(order):
    required_fields = ['user', 'status', 'amount']
    for field in required_fields:
        if field not in order:
            raise KeyError(f"Отсутствует обязательное поле: {field}")
    if not isinstance(order['user'], str):
        raise TypeError("Поле 'user' должно быть строкой.")
    if not isinstance(order['status'], str):
        raise TypeError("Поле 'status' должно быть строкой.")
    amount = order['amount']
    if not isinstance(amount, (int, float)):
        raise TypeError("Поле 'amount' должно быть числом.")
    if amount < 0:
        raise ValueError("Поле 'amount' не может быть отрицательным.")
    return True
