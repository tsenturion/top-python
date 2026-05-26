"""
0607_Рекурсия
"""

def factorial(n):
    """Рекурсивная функция для вычисления факториала числа n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120