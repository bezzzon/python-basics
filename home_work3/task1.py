"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Division by zero is not allowed!')


divide(int(input('Please input number #1: ')), int(input('Please input number #2: ')))
