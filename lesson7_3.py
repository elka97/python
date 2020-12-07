"""". Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке."""


class Cell:
    n = 0

    def __init__(self, param):
        self.n = param

    def __add__(self, other):
        if not isinstance(other, Cell):
            print(f"Wrong parameter type {type(other)}")
            return
        return self.n + other.n

    def __sub__(self, other):
        if not isinstance(other, Cell):
            print(f"Wrong parameter type {type(other)}")
            return
        if self.n - other.n > 0:
            return self.n - other.n
        print(f"Difference less than 0 ({self.n}, {other.n})")

    def __mul__(self, other):
        if not isinstance(other, Cell):
            print(f"Wrong parameter type {type(other)}")
            return
        return self.n * other.n

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            print(f"Wrong parameter type {type(other)}")
            return
        return int(self.n / other.n)

    def make_order(self, cells_in_row):
        nl = "n"
        result = []
        total = self.n
        for el in range(0, self.n, cells_in_row):
            result.append(f"{'*' * cells_in_row}")
            if cells_in_row < total:
                total -= cells_in_row
        result.append(f"{'*' * total}")
        s = f"\{nl}".join(result)
        return s


a = Cell(12)
b = Cell(5)

print(f"Cell A: {a.n} Cell B: {b.n}")
print(f"Sum: {a.__add__(b)}")
print(f"Subtract a-b: {a.__sub__(b)}")
print(f"Subtract b-a: {b.__sub__(a)}")
print(f"Multiply: {a.__mul__(b)}")
print(f"Divide a/b: {a.__truediv__(b)}")
print(f"Divide b/a: {b.__truediv__(a)}")
print(f"make_order: {a.make_order(b.n)}")
