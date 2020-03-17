class kletka:
    def __init__(self, kol):
        self.kol = int(kol)
    def __str__(self):
        return f"Кол-во: {self.kol} "
    def __add__(self, other):
        return kletka(self.kol + other.kol)
    def __sub__(self, other):
        if self.kol - other.kol > 0:
            return kletka(self.kol - other.kol )
        else:
            return "Клеток не хватает"
    def __mul__(self, other):
        return f"Умножение {kletka(self.kol * other.kol)}"
    def __truediv__(self, other):
        return kletka(round(self.kol//other.kol))
    def make_order(self, oops):
        row = " "
        for i in range(int(self.kol / oops)):
            row += f'{"*" * oops} \\n'
        row += f'{"*" * (self.kol % oops)}'
        return row

kl_1 = kletka(12)
kl_2 = kletka(11)
print(kl_1)
print(kl_2)
print(kl_1+kl_2)
print(kl_1-kl_2)
print(kl_1*kl_2)
print(kl_1/kl_2)
print(kl_1.make_order(12))