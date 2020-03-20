class Chislo:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
    def __add__(self, other):
        return f'Сумма: z = {self.a + other.a} + {self.b + other.b}*i'
    def __sub__(self, other):
        return f'Разность: z = {self.a - other.a} + {self.b - other.b} *i'
    def __mul__(self, other):
        return f'Произведение: z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} *i'
    def __str__(self):
        return f'Число: z = {self.a} + {self.b} *i'


z_1 = Chislo(1, -2)
z_2 = Chislo(3, 4)
print(z_1)
print(z_2)
print("*" * 20)
print(z_1 + z_2)
print(z_1 - z_2)
print(z_1 * z_2)