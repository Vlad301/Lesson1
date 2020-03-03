def g():
        var_1 = float(input("Введите первое число: "))
        var_2 = float(input("Введите второе число: "))
        if var_2 == 0:
            return "На ноль делить нельзя"
        else:
            return var_1/var_2
res = g()
print(res)