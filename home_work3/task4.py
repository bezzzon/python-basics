"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


print('----- Implementation with using ** operator -----')
print(my_func_1(int(input('Please input positive number: ')), int(input('Please input negative number: '))))
print('----- Implementation without using ** operator -----')
print(my_func_2(int(input('Please input positive number: ')), int(input('Please input negative number: '))))
