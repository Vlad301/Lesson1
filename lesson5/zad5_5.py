set = open("chisla.txt", "w")
num = []
num_2 = []
try:
    line = input("Цифры через пробел: ")
    num = line.split()
    num_2 = map(int, num)
    set.writelines(num)
    print(f"Сумма: {sum(num_2)}")
except ValueError:
    print("Ошибка ввода! Необходимо ввести цифры через пробел!")

set.close()
