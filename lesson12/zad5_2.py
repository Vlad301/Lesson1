my_list = [7, 5, 3, 3, 2]
print(f"Начальный список : {my_list}")
print("-----------------------------")
b = int(input("Введите число (Завершение цикла 000): "))
while b != 000:
    for i in range(len(my_list)):
        if b == my_list[i]:
            my_list.insert(i + 1, b)
            break
        elif b < my_list[i] and b > my_list[i + 1]:
            my_list.insert(i + 1, b)
        elif b < my_list[-1]:
            my_list.append(b)
        elif b > my_list[0]:
            my_list.insert(0, b)
    print(my_list)
    b = int(input("Введите число (Завершение цикла 000): "))
