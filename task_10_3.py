class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if self.cell - other.cell > 0 else 'Вычитание невозможно'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell) if self.cell // other.cell > 0 else 'Деление невозможно'

    def __truediv__(self, other):
        return Cell(self.cell // other.cell) if self.cell // other.cell > 0 else 'Деление невозможно'

    def make_order(self, row):
        str_1 = f'{"*" * row}\n'
        return f'{str_1 * (self.cell // row)}{"*" * (self.cell % row)}\n'


cell_1 = Cell(12)
cell_2 = Cell(11)
print('Сложение ', cell_1 + cell_2)
print('Вычитание ', cell_1 - cell_2)
print('Вычитание ', cell_2 - cell_1)

print('Умножение ', cell_1 * cell_2)
print('Целочисленное деление', cell_1 // cell_2)
print('Целочисленное деление', cell_2 // cell_1)
print('Деление', cell_1 / cell_2)
print('Деление', cell_2 / cell_1)
print(cell_1.make_order(5))
