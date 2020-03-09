with open('zp.txt', 'r') as my_file:
    zp = []
    cash = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           cash.append(i[0])
        zp.append(i[1])
print(f'Оклад меньше 20.000 {cash}, средний оклад {sum(map(int, zp)) / len(zp)}')