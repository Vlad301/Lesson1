class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def s_palto(self):
        return f"расход на пальто: {round(self.width / 6.5 + 0.5)}"

    def s_suit(self):
        return f"расход на костюм: {self.height * 2 + 0.3}"

    @property
    def s_all(self):
        return str(f'Всего ткани: '
                   f' {round(self.width / 6.5 + 0.5) + round(self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.s_palto_1 = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Ткани на пальто: {self.s_palto_1}'


class Suit(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.s_kurtka_1 = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Ткани на костюм {self.s_kurtka_1}'

coat = Coat(2, 4)
suiiit = Suit(1, 2)
print(coat)
print(suiiit)
print(coat.s_all)
print(suiiit.s_all)
print(suiiit.s_palto())
print(suiiit.s_suit())