from functools import reduce
set = [i for i in range(100, 1001) if i % 2 == 0]
print(f"Исходный список: {set}")

def my_func (a ,b):
    return a*b
print(f"Результат перемножения: {reduce(my_func, set)}")