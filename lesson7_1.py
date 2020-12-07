"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    matrix = []

    def __init__(self, arg):
        self.matrix = arg

    def __str__(self):
        sb = f"Matrix ({[el for el in self.matrix]})"
        return sb

    def __add__(self, other):
        if not isinstance(other, Matrix):
            print(f"Wrong parameter type {type(other)}")
            return

        if len(other.matrix) > len(self.matrix):
            long_list = other.matrix
            short_list = self.matrix
        else:
            long_list = self.matrix
            short_list = other.matrix

        result = long_list

        for i, el in enumerate(short_list):
            try:
                xx = self.__sum_lists(el, long_list[i])
                result[i] = xx
            except:
                print(f"Exception on {i}")
        return Matrix(result)

    def __sum_lists(self, l1, l2):
        if len(l1) < len(l2):
            for i, el in enumerate(l1):
                l2[i] += l1[i]
            return l2
        if len(l1) >= len(l2):
            for i, el in enumerate(l2):
                l1[i] += l2[i]
            return l1
        return


a = Matrix([[31, 22], [37, 43], [51, 86]])
print(a)
b = Matrix([[3, 5, 8, 3, 9], [8, 3, 7, 1, 3]])
print(b)

addition = a.__add__(b)
print(addition)

addition = a.__add__(Matrix([[1, 9], [8]]))
print(addition)