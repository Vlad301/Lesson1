from sys import argv

name_file, work, stavka, premia = argv
try:
    work = int(work)
    stavka = int(stavka)
    premia = int(premia)
    zp = (work * stavka) + premia
    print("Выработка в часах: ", work)
    print("Ставка в час: ", stavka)
    print("Премия: ", premia)
    print(f"Зарплата: {zp}")
except ValueError:
    print("Enter numbers!")
