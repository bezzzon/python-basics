"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

eng_ru_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


def translate(record):
    tokens = record.split()
    tokens[0] = eng_ru_dict[tokens[0]]
    return ' '.join(tokens)


with open('task4.txt', 'r', encoding='utf-8') as f:
    with open('task4_tr.txt', 'w', encoding='utf-8') as f_tr:
        for line in f:
            f_tr.write(translate(line) + '\n')

print('Conversion completed')
