"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

arr = []

while True:
    el = input('Please input some array element: ')
    # по команде stop прерываем заполнение списка
    if el != "stop":
        arr.append(el)
    else:
        break

arr_even = arr[::2]  # получаем список с четными элементами базового списка
arr_odd = arr[1::2]  # получаем список с нечетными элементами базового списка

new_arr = []  # новый список для добавления элементов с измененным порядком
i = 0  # переменная-индекс
# цикл ограничен количеством замен. Так как замены парные, то замен в 2 раза меньше,
# чем количество элементов базового списка.
while i < len(arr) // 2:
    new_arr.append(arr_odd[i])  # сначала добавляем элемент из списка с четными
    new_arr.append(arr_even[i])  # далее добавляем элемент из списка с нечетными
    i += 1

# если количество элементов базового списка нечетное, то последний элемент остается на своем месте
if len(arr) % 2 != 0:
    new_arr.append(arr_even[-1])

print(f'Initial array: {arr}')
print(f'Formatted array: {new_arr}')
