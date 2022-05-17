"""Это тестовая программа на соответствие кода PEP8 и т.п"""
import math

MESSAGE = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return math.sqrt(number)


def calc(your_number):
    """Проверяет, положительно ли число."""
    if your_number <= 0:
        return
    print(f'Мы вычислили корень квадратный из введенного вами '
          f'числа. Это будет: {calculate_square_root(your_number)}')


print(MESSAGE)
calc(25.5)
