class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"запуск отрисовки {self.title}"


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"запуск отрисовки | метод PEN | {self.title}"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"запуск отрисовки | метод Pencil | {self.title}"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"запуск отрисовки | метод Handle | {self.title}"
pen = Pen("Ручка")
pencil = Pencil ("Карандаш")
handle = Handle("Маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())