class Noli:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def nullik(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = Noli(10, 100)
print(Noli.nullik(10, 0))
print(Noli.nullik(10, 0.1))
print(div.nullik(100, 0))