def my_sum ():
    result = 0
    over = True
    while over == True:
        number = input("Вводите числа через пробел. Для выхода введити 000: ").split()

        sum = 0
        for i in range(len(number)):
            if number[i] == '000':
                over = False
                break
            else:
                sum = sum + int(number[i])
        result = result + sum
        print("*"*50)
        print(f"Сумма: {result}")
    print(f"Конечная сумма: {result}")
    print("*" * 50)


my_sum()