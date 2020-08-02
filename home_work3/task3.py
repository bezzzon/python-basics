"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    arr = [a, b, c]
    arr.remove(min(arr))
    return sum(arr)


print(my_func(5, 2, 6))
