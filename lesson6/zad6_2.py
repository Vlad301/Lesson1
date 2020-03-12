class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def set(self):
        return self._lenght * self._width


class Massa(Road):
    def __init__(self, _lenght, _width, _mass, _sm):
        super().__init__(_lenght, _width)
        self._mass = _mass
        self._sm = _sm
    def choko(self):
        return self._lenght * self._width * self._mass * self._sm


a = Massa(10, 20, 2, 5)
print(f"Расчет асфальта: {a.choko()}")
