stroka = input("Введите строчку:")
mas = []
nom = 1
for h in range(stroka.count(" ") + 1):
    mas = stroka.split(" ")
    if len(str(mas)) <=10:
        print(f"{mas[h]} : {nom}")
        nom +=1
    else:
        print(f"{mas[h][0:10]} : {nom}")
        nom+=1

