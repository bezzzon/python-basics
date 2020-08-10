"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

import itertools


def start_count_iterator(start, end):
    for i in itertools.count(start):
        if i < end:
            print(i)
        else:
            break


def start_cycle_iterator(iterable, end):
    i = 0
    for char in itertools.cycle(iterable):
        if i < end:
            print(char)
        else:
            break
        i += 1


print('----- Cycle iterator -----')
start_count_iterator(3, 10)
print('----- Count iterator -----')
start_cycle_iterator('I am terminator', 51)
