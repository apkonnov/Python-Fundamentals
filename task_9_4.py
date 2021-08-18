import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, sp):
        self.speed = sp
        return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'

    def stop(self):
        self.speed = 0
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} {direction}'

    def show_speed(self):
        return f'Автомобиль {self.name} движется со скоростью {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость превышена! {Car.show_speed(self)}'
        return Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость превышена! {Car.show_speed(self)}'
        return Car.show_speed(self)


class PoliceCar(Car):
    pass


town_car = TownCar(50, 'black', 'Mazda', False)
sport_car = SportCar(60, 'red', 'Ferrari', False)
work_car = WorkCar(90, 'gray', 'Largus', False)
police_car = PoliceCar(110, 'white', 'Vesta', True)
for class_name in (town_car, sport_car, work_car, police_car):
    print(class_name.name, class_name.color, class_name.speed, class_name.is_police)
    print(class_name.show_speed())
    print(class_name.turn(random.choice(('повернул направо', 'повернул налево', 'движется прямо', 'поехал назад'))))
    print(class_name.go(random.randrange(10, 110)))
    print(class_name.stop(), end='\n\n')
