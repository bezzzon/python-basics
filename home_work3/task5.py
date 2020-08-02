"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def get_sum(data):
    for i in range(len(data)):
        data[i] = int(data[i])
    return sum(data)


summary = 0
is_inputting = True

while is_inputting:
    numbers_string = input('Please input digits separating them via spaces. Use "q" symbol to stop the program: ')
    numbers = numbers_string.split()
    if numbers.count('q') > 0:
        numbers = numbers[:numbers.index('q')]
        is_inputting = False
    try:
        summary += get_sum(numbers)
    except (ValueError, TypeError):
        print(f'Array contains wrong type elements {numbers}, please try again.')

print('Total summary: ', summary)
