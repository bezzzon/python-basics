"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

import functools


def multiply(a, b):
    return a * b


base_list = [num for num in range(100, 1001) if num % 2 == 0]

print(functools.reduce(multiply, base_list))