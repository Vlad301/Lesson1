my_list = [10, 12, 10, 12, 5, 3, 212, 3, 521]
set = [el for el in my_list if my_list.count(el) < 2]
print(f"Неповторяющиеся числа: {set}")