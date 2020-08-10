"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_words(text):
    return len(text.split())


with open('task2.txt', 'r') as f:
    content = f.readlines()
    print('Total lines:', len(content))
    print('------------------------')
    for i in range(len(content)):
        print(f'Line {i+1} contains: {count_words(content[i])} words')
