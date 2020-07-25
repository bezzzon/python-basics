"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

day = 0
not_achieved = True
current = int(input('Please input number of kilometers to start with: '))
goal = int(input('Please input your goal in kilometers: '))

while not_achieved:
    day += 1
    if current < goal:
        current += current * 0.1
    else:
        not_achieved = False

print(f'On the day {day} you will achieve your goal of {goal} km.\nKeep going !')
