vur = float(input("Выручка фирмы: "))
izd = float(input("Издержки фирмы: "))
if vur > izd:
    print(f"Фирма работает с прибылью. Рентабельность: {vur / izd}")
    soldiers = int(input("Количество сотрудников: "))
    print(f"Прибыль на одного сотрудника: {vur / soldiers}")
elif vur == izd:
    print("Фирма работает ровно (без убытка и прибыли)")
else:
    print("Фирма работает в убыток")