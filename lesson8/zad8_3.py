class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')

            except:
                print(f"Недопустимое значение - строка и булево")
                quest = input(f'Попробовать еще раз? + или - ')
                if quest == '+':
                    print(try_except.my_input())
                elif quest == '-':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(0)
print(try_except.my_input())