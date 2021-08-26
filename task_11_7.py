class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'({self.a} - {abs(self.b)}i)'
        else:
            return f'({self.a} + {self.b}i)'

    def __add__(self, other):
        return Complex(round(self.a + other.a, 3), round(self.b + other.b, 3))

    def __mul__(self, other):
        return Complex(round(self.a * other.a - self.b * other.b, 3), round(self.a * other.b + other.a * self.b, 3))


complex_1 = Complex(5.5, 3.3)
print(complex_1)
complex_2 = Complex(-6, 12)
print(complex_2)
complex_3 = Complex(4, -8)
print(complex_3)
print()
print(complex_1 + complex_2)
print(complex_1 + complex_3)
print(complex_2 + complex_3)
print(complex_1 + complex_2 + complex_3)

print()
print(complex_1 * complex_2)
print(complex_1 * complex_3)
print(complex_2 * complex_3)
print(complex_1 * complex_2 * complex_3)
