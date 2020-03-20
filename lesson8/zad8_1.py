class Data:
    def __init__(self, year):
        self.year = str(year)

    @classmethod
    def a(cls, year):
        chislo = []

        for i in year.split():
            if i != ":":
                chislo.append(i)

        return int(chislo[0]), int(chislo[1]), int(chislo[2])

    @staticmethod
    def wh(number, month, years):
        if 1 <= number <= 31:
            if 1 <= month <= 12:
                if 2000 <= years <= 2020:
                    return f"Дата правильная: {number} - {month} - {years}"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"

        else:
            return f"Неправильный день"

    def tak(self):
        return f"Дата: {Data.wh(self.year)}"
seg = Data("11 : 21 : 10")
print(seg)
print(Data.wh(12, 12, 2001))
print(seg.wh(12, 31, 2003))
print(Data.a("10 : 12 : 12"))
print(seg.a("31 : 21 : 3112"))
