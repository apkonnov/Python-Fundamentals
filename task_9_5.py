class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки объекта {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}. Запуск отрисовки объекта.')


class Handle(Stationery):
    def draw(self):
        print(f'Объект {self.title}. Запуск отрисовки.')


Stationery_1 = Stationery('Канцелярская принадлежность')
Stationery_1.draw()
Pen_1 = Pen('Ручка')
Pen_1.draw()
Pencil_1 = Pencil('Карандаш')
Pencil_1.draw()
Handle_1 = Handle('Маркер')
Handle_1.draw()
