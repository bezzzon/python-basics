"""
Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

a = 1.25
b = 'Python'
c = 1 > 0

print(a, b, c)

a = float(input('Please input float number: '))
b = input('Please input any string: ')
c = bool(input('Please input boolean (True/False): '))

print(a, b, c)
