"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def calc_salary():
    hours = int(sys.argv[1])  # просто берем полное количество отработанных часов
    salary_per_hour = float(sys.argv[2])
    bonus = float(sys.argv[3])
    return hours * salary_per_hour + bonus


print(calc_salary())
# C:\Users\HP\PycharmProjects\python-basics\home_work4>python task1.py 20 5000 1020.45
# 101020.45
