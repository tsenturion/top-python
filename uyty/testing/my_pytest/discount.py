def validate_price(price):
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Цена должна быть положительным числом.")
    return True

def validate_discount(discount):
    if not isinstance(discount, (int, float)) or not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть от 0 до 100 процентов.")
    return True

def apply_discount(price, discount):
    validate_price(price)
    validate_discount(discount)
    return round(price * (1 - discount / 100), 2)

def calculate_cart_total(cart):
    """
    cart: список словарей вида {'name': str, 'price': float, 'quantity': int}
    """
    total = 0
    for item in cart:
        if not isinstance(item, dict):
            raise TypeError("Каждый элемент корзины должен быть словарём.")
        if 'price' not in item or 'quantity' not in item:
            raise KeyError("Каждый товар должен содержать 'price' и 'quantity'.")
        validate_price(item['price'])
        if not isinstance(item['quantity'], int) or item['quantity'] <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")
        total += item['price'] * item['quantity']
    return round(total, 2)
