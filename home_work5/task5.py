"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('task5.txt', 'w') as f:
    f.write(input('Please input numbers separated by space then press enter: '))

with open('task5.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))
    print(sum(numbers))
