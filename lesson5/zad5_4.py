rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('zad5_4.txt', 'r') as set:
    for i in set:
        i = i.split()
        new_file.append(rus[i[0]] + " " + i[1] + " " + i[2])
    print(new_file)

with open('zad5_4_1.txt', 'w') as set_2:
    set_2.writelines(new_file)
