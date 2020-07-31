"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

seconds = int(input('Please input number of seconds: '))

hours = seconds // 3600
if hours > 0:
    seconds -= hours * 3600  # leaving seconds without full hours

minutes = seconds // 60
if minutes > 0:
    seconds -= minutes * 60  # leaving minutes without full minutes

print(f'{hours:02}:{minutes:02}:{seconds:02}')
