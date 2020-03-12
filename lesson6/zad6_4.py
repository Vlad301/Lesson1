class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} Поехала"

    def stop(self):
        return f"{self.name} Остановилась"

    def turn_right(self):
        return f"{self.name} повернул(а) на право"

    def turn_left(self):
        return f"{self.name} повернул(а) на лево"

    def show_speed(self):
        return f"{self.name} имеет на спидометре {self.speed}"


class Town_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 60:
            print("Привышение скорости!")
        else:
            print("Скорость удовлетворяет правилам движения")

        return f"{self.name} имеет на спидометре {self.speed}"


class Sport_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class Work_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print("Привышение скорости!")
        else:
            print("Скорость удовлетворяет правилам движения")
        return f"{self.name} имеет на спидометре {self.speed}"
class Police_car(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f"Это полиция"
        else:
            return f"Не полиция"

bmw = Town_car(210, "Blue", "BMW X5", False)
amg = Sport_car(300, "Yellow", "Mercedec e63 AMG", False)
kia = Work_car(30, "Green", "Kia Ceed", True)
lada = Police_car(100, "White", "Lada Priora", True)
print(bmw.turn_left())
print("*" * 30)
print(amg.turn_right())
print("*" * 30)
print(lada.police())
print("*" * 30)
print(amg.show_speed())
print("*" * 30)
print(bmw.show_speed())
print("*" * 30)
print(f"{lada.name} полицейская? {lada.is_police}")
print("*" * 30)
print(f"{bmw.name} полицейская? {bmw.is_police}")




