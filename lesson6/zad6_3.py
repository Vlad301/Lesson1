class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name, self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


b = Position("Vlad", "Epishin", "Operator", 2000, 2100)
print(b.get_full_name())
print(b.position)
print(b.get_total_income())
