"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, income):
        """income in the format {"wage": wage, "bonus": bonus}"""
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._Worker__income['wage'] + self._Worker__income['bonus']


p = Position('Ivan', 'Petrov', 'doctor', {'wage': 50000, 'bonus': 10000})
print(p.name)
print(p.surname)
print(p.position)
print(p._Worker__income)
print(p.get_full_name())
print(p.get_total_income())
