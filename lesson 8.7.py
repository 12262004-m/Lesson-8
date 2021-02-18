class ComplexNumbers:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.k = 'a+b*i'
    def __add__(self, other):
        return f'Сумма 1ого комплексного числа и 2ого комплексного числа равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
         return f"Произведение 1ого комплексного числа и 2ого комплексного числа равно: {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}*i"
    def __str__(self):
        return f'Комплексное число: {self.a} + {self.b} * i'

k1 = ComplexNumbers(2, 6)
k2 = ComplexNumbers(1, 3)
print(k1)
print(k1+k2)
print(k1*k2)

