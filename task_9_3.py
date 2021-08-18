class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


employee = Position('Иван', 'Иванов', 'Оператор', 11000, 25000)
print(employee.name)
print(employee.surname)
print(employee.position)
print(employee._income)
print(employee.get_full_name(), employee.get_total_income())
