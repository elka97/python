"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_required(self):
        pass


class Suit(Clothes):
    H = 0.0

    def __init__(self, name, param):
        super().__init__(name)
        self.H = param

    @property
    def cloth_required(self):
        return (2 * self.H + 0.3)


class Coat(Clothes):
    V = 0.0

    def __init__(self, name, param):
        super().__init__(name)
        self.V = param

    @property
    def cloth_required(self):
        return (self.V / 6.5 + 0.5)


a = Suit("Black suit", 180)
b = Coat("Blue coat", 46)

print(f"{a.name} {a.cloth_required} sq.mt")
print(f"{b.name} {b.cloth_required} sq.mt")
print(f"Total cloth: {a.cloth_required + b.cloth_required}")

c = Coat("Plus white coat", 88)
print(f"{c.name} {c.cloth_required} sq.mt")
print(f"Total cloth: {a.cloth_required + b.cloth_required + c.cloth_required}")