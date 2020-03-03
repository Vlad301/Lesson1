a = abs(int(input("Введите целое положительное число: ")))
b = int(input("Введите целое отрицательное число: "))
c = 1


def my_func(a, b):
    return a ** b


print(f"Результат через my_func: {my_func(a, b):.4f}")

while b < 0:
    c /= a
    b += 1
print(f"Результат через цикл: {c:.4f}")
