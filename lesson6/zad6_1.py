import time


class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):

        while True:
            j = 0
            for i in self.__color:
                print(f"Свет: {i} | номер цвета: {j} ")
                j += 1
                if j % 2 == 1:
                    time.sleep(7)
                 
                else:
                    time.sleep(2)


a = TrafficLight()
a.running()
