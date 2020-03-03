a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))


def my_func(*args):
    if a > c and b > c:
        return a + b
    elif a > b and c > b:
        return a + c
    elif b > a and c > a:
        return b + c


print(my_func(a, b, c))
