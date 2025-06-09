# test_discount.py

import pytest
from my_pytest.discount import apply_discount, calculate_cart_total, validate_price, validate_discount
# ----- Фикстуры -----
@pytest.fixture
def cart():
    return [
        {"name": "Book", "price": 500.0, "quantity": 2},
        {"name": "Pen", "price": 50.0, "quantity": 3}
    ]

# ----- Тесты функции apply_discount -----
def test_apply_discount_valid():
    assert apply_discount(1000, 10) == 900.0

def test_apply_discount_zero():
    assert apply_discount(1000, 0) == 1000.0

def test_apply_discount_full():
    assert apply_discount(1000, 100) == 0.0

def test_apply_discount_invalid_price():
    with pytest.raises(ValueError):
        apply_discount(-200, 10)

def test_apply_discount_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(200, 150)

# ----- Тесты функции calculate_cart_total -----
def test_calculate_cart_total(cart):
    # 500*2 + 50*3 = 1000 + 150 = 1150
    assert calculate_cart_total(cart) == 1150.0

def test_cart_with_invalid_quantity():
    with pytest.raises(ValueError):
        calculate_cart_total([{"name": "Book", "price": 100, "quantity": 0}])

def test_cart_with_missing_fields():
    with pytest.raises(KeyError):
        calculate_cart_total([{"name": "Pen", "price": 20}])  # Нет quantity

def test_cart_with_invalid_item_type():
    with pytest.raises(TypeError):
        calculate_cart_total(["not a dict"])

# ----- Валидация -----
def test_validate_price():
    assert validate_price(100) is True

def test_validate_price_negative():
    with pytest.raises(ValueError):
        validate_price(-10)

def test_validate_discount_range():
    assert validate_discount(50) is True

def test_validate_discount_out_of_range():
    with pytest.raises(ValueError):
        validate_discount(120)
