"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self, weight_per_m2, thickness):
        """weight_per_m2 in kg, thickness in centimeter, returns weight in ton"""
        return self.__length * self.__width * weight_per_m2 * thickness / 1000


road = Road(20, 5000)
print(road.calc_weight(25, 5))
