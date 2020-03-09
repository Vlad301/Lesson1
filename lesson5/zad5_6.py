spisok = {}
with open('zad5_6.txt', 'r') as init_f:
    for line in init_f:
        pred, le, pra, lab = line.split()
        spisok[pred] = int(le) + int(pra) + int(lab)
    print(f'Часы: {spisok}')