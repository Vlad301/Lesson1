numbers = int(input("Введите число элементов списка: "))
list1 = []
i = 0
k = 0
while i < numbers:
    list1.append(int(input(f"Введите {i} элемент списка: ")))
    i += 1
for check in range(int(len(list1) / 2)):
    list1[k], list1[k + 1] = list1[k + 1], list1[k]
    k += 2
print(list1)
