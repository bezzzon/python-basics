"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

is_writing = True
with open('task1.txt', 'a') as f:
    while is_writing:
        text = input('Please input text: ')
        is_writing = False if len(text) == 0 else f.write(text + '\n')

