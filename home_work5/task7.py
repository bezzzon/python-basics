"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json


def get_company_name(record):
    return record.split()[0]


def get_profit(record):
    return float(record.split()[2]) - float(record.split()[3])


result = [{}, {}]

with open('task7.txt', 'r', encoding='utf-8') as f:
    # если реализовывать именно построчное считывание, а не считать разом в массив
    sum_profit = 0
    i = 0
    for line in f:
        i += 1
        profit = get_profit(line)
        name = get_company_name(line)
        if profit >= 0:
            sum_profit += get_profit(line)
        result[0][name] = profit
    result[1]['average_profit'] = sum_profit / i

with open('task7_result.txt', 'w', encoding='utf-8') as f:
    json.dump(result, f)

print('Conversion completed')
