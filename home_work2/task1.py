"""
 Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента.
 Использовать функцию type() для проверки типа.
 Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

arr = [1, True, 2.09, "value", None]
for i in arr:
    print(type(i))
