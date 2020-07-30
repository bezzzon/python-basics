"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# implementation with dict
seasons = {
    'winter': (1, 2, 12),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}

month = int(input('Please input month from 1 to 12: '))
for season, months in seasons.items():
    if month in months:
        print(f'Month {month} belongs to {season}')
        break

# implementation with list
seasons = [
    'winter', 'winter',
    'spring', 'spring', 'spring',
    'summer', 'summer', 'summer',
    'autumn', 'autumn', 'autumn',
    'winter'
]

print(f'Month {month} belongs to {seasons[month - 1]}')
