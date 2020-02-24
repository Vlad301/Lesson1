a = float(input("Первый день в км: "))
b = float(input("Желательный результат в км: "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = a
print(f"Вы достигнете требуемых показателей на {result_days} день")