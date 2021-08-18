class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_meter, thickness):
        return self._length * self._width * mass_meter * thickness


asphalt_mass = Road(20, 5000)
print(asphalt_mass.calc_mass(25, 5)/1000, 'т')
