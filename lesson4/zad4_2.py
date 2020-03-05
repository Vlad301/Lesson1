my_list = [1, 2, 100, 500, 31, 3114, 3]
my_new_list = [a for num, a in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')