"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

threshold_amount = 20000


def get_salary(record):
    return float(record.split('***')[1])


def get_name(record):
    return record.split('***')[0]


with open('task3.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    for employee in content:
        if get_salary(employee) <= threshold_amount:
            print(get_name(employee), 'has the salary less than', threshold_amount)
    print(f'The average salary is: {sum(list(map(get_salary, content))) / len(content):.2f}')
