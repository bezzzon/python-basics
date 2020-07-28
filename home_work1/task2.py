"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

threshold = 10  # variable to check if we need leading zero
seconds = int(input('Please input number of seconds: '))

hours = seconds // 3600
if hours > 0:
    seconds -= hours * 3600  # leaving seconds without full hours

if hours < threshold:
    hours = f'0{hours}'  # convert hours to text based on pattern

minutes = seconds // 60
if minutes > 0:
    seconds -= minutes * 60  # leaving minutes without full minutes

if minutes < threshold:
    minutes = f'0{minutes}'  # convert minutes to text based on pattern

if seconds < threshold:
    seconds = f'0{seconds}'  # convert seconds to text based on pattern

print(f'{hours}:{minutes}:{seconds}')
