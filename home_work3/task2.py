"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person_info(first_name, last_name, dob, city, email='', phone=''):
    return f'Name: {first_name}, last name: {last_name}, ' \
           f'date of birth: {dob}, city: {city}, email: {email}, phone: {phone}'


print(person_info(last_name='Smith', dob='01 April 1970', city='Moscow', phone='12-34-567', first_name='Ivan'))
