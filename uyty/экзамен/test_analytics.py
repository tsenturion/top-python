# test_analytics_unittest.py
import unittest
from analytics import (
    filter_orders,
    calculate_total_revenue,
    count_orders_by_user,
    validate_order
)

class TestAnalytics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Подготовка тестовых данных (вызывается один раз для всех тестов)"""
        cls.sample_orders = [
            {"id": 1, "user": "Alice", "amount": 100, "status": "completed"},
            {"id": 2, "user": "Bob", "amount": 200, "status": "pending"},
            {"id": 3, "user": "Alice", "amount": 50, "status": "completed"},
            {"id": 4, "user": "Charlie", "amount": 300, "status": "cancelled"},
        ]

    # Тесты для filter_orders
    def test_filter_orders_completed(self):
        """Тест фильтрации заказов по статусу 'completed'"""
        result = filter_orders(self.sample_orders, "completed")
        self.assertEqual(len(result), 2)
        self.assertTrue(all(order["status"] == "completed" for order in result))
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 3)

    def test_filter_orders_empty_result(self):
        """Тест фильтрации с несуществующим статусом"""
        result = filter_orders(self.sample_orders, "shipped")
        self.assertEqual(len(result), 0)
        self.assertIsInstance(result, list)

    def test_filter_orders_invalid_status_type(self):
        """Тест с неправильным типом статуса"""
        with self.assertRaises(TypeError):
            filter_orders(self.sample_orders, 123)

    # Тесты для calculate_total_revenue
    def test_calculate_total_revenue(self):
        """Тест подсчета общей выручки"""
        self.assertEqual(calculate_total_revenue(self.sample_orders), 650)
        self.assertIsInstance(calculate_total_revenue(self.sample_orders), int)

    def test_calculate_total_revenue_empty(self):
        """Тест с пустым списком заказов"""
        self.assertEqual(calculate_total_revenue([]), 0)

    def test_calculate_total_revenue_negative_amount(self):
        """Тест с отрицательной суммой заказа"""
        with self.assertRaises(ValueError):
            calculate_total_revenue([{"amount": -100}])

    # Тесты для count_orders_by_user
    def test_count_orders_by_user(self):
        """Тест подсчета заказов по пользователям"""
        result = count_orders_by_user(self.sample_orders)
        expected = {"Alice": 2, "Bob": 1, "Charlie": 1}
        self.assertDictEqual(result, expected)
        self.assertIsInstance(result, dict)

    def test_count_orders_by_user_empty(self):
        """Тест с пустым списком заказов"""
        self.assertDictEqual(count_orders_by_user([]), {})

    # Тесты для validate_order
    def test_validate_order_correct(self):
        """Тест валидации корректного заказа"""
        order = {"id": 1, "user": "Alice", "amount": 100, "status": "completed"}
        self.assertTrue(validate_order(order))

    def test_validate_order_missing_field(self):
        """Тест с отсутствующим обязательным полем"""
        with self.assertRaises(ValueError):
            validate_order({"user": "Alice", "amount": 100})

    def test_validate_order_invalid_user_type(self):
        """Тест с неправильным типом пользователя"""
        with self.assertRaises(TypeError):
            validate_order({"id": 1, "user": 123, "amount": 100, "status": "completed"})

    def test_validate_order_invalid_amount_value(self):
        """Тест с отрицательной суммой"""
        with self.assertRaises(ValueError):
            validate_order({"id": 1, "user": "Alice", "amount": -100, "status": "completed"})

    def test_validate_order_invalid_amount_type(self):
        """Тест с неправильным типом суммы"""
        with self.assertRaises(ValueError):
            validate_order({"id": 1, "user": "Alice", "amount": "100", "status": "completed"})

if __name__ == '__main__':
    unittest.main(verbosity=2)