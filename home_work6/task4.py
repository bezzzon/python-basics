"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} has started to move')

    def stop(self):
        print(f'Car {self.name} has stopped')

    def turn(self, direction):
        print(f'Car {self.name} has turned to {direction}')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')

    def to_string(self):
        return f'Name is {self.name}, speed is {self.speed}, color is {self.color}, police car - {self.is_police}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'The speed of {self.name} is too high ({self.speed}) for the class of car "TownCar"')
        else:
            print(f'Current speed of {self.name} is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'The speed of {self.name} is too high ({self.speed}) for the class of car "WorkCar"')
        else:
            print(f'Current speed of {self.name} is {self.speed}')


class PoliceCar(Car):
    pass


town_car1 = TownCar('Mazda 3', 60, 'black', False)
town_car2 = TownCar('Infinity', 75, 'yellow', False)
sport_car = SportCar('Ferrari', 300, 'red', False)
work_car1 = SportCar('Ford', 35, 'grey', False)
work_car2 = SportCar('Ford', 55, 'green', False)
police_car = SportCar('Toyota', 150, 'silver', True)

print(town_car1.to_string())
print(town_car2.to_string())
print(sport_car.to_string())
print(work_car1.to_string())
print(police_car.to_string())
print('--------------------------------')
town_car1.go()
town_car1.turn('NORTH')
town_car1.stop()
print('--------------------------------')
town_car1.show_speed()
town_car2.show_speed()
police_car.show_speed()
