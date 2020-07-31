"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

num = int(input('Please input valid positive number: '))
max_digit = 0

while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    num //= 10

print(max_digit)
