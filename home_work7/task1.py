"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if not self.__check_if_matrix_valid() or not other.__check_if_matrix_valid():
            return 'Incorrect matrix/matrices provided.'
        result = []
        if self.__check_if_same_size(other):
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i])):
                    result[i].append(self.matrix[i][j] + other.matrix[i][j])
        else:
            return 'Matrices have different sizes and cannot be added to each other.'
        return Matrix(result)

    def __check_if_matrix_valid(self):
        length = len(self.matrix[0])
        for m in range(1, len(self.matrix)):
            if len(self.matrix[m]) != length:
                return False
        return True

    def __check_if_same_size(self, other):
        self_i = len(self.matrix)
        other_i = len(other.matrix)
        if self_i == other_i:
            for i in range(self_i):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    return False
        else:
            return False
        return True

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += ' '.join(list(map(str, row))) + '\n'
        return result[:-1]


m1 = Matrix([[1, 2, 4], [3, 4, 5], [6, 7, 8]])
m2 = Matrix([[9, 8, 6], [7, 6, 5], [4, 3, 2]])
print(m1 + m2)
