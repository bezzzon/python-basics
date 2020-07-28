"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

# Implemented with positive numbers only
num = int(input('Please input valid positive number: '))
double_num = int(str(num) * 2)
triple_num = int(str(num) * 3)
print(f'Sum of {num} + {double_num} + {triple_num} = {num + double_num + triple_num}')
