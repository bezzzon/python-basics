"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.title()


def is_word_valid(word):
    for char in list(word):
        if ord(char) < 97 or ord(char) > 122:
            print(f'Unexpected character in word "{word}" detected!')
            return False
    return True


string = 'london is the capital of great britain'
words = string.split()

for i in range(len(words)):
    if is_word_valid(words[i]):
        words[i] = int_func(words[i])
    else:
        break

print(' '.join(words))
