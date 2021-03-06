"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    # @property
    def calc_material(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        super().__init__('coat')
        self.size = size

    @property
    def calc_material(self):
        return round(self.size/6.5 + 0.5, 2)


class Jacket(Clothes):

    def __init__(self, height):
        super().__init__('jacket')
        self.height = height

    @property
    def calc_material(self):
        return 2 * self.height + 0.3


coat = Coat(56)
print(coat.title, '-', coat.calc_material)
print('----------------------')
jacket = Jacket(175)
print(jacket.title, '-', jacket.calc_material)
