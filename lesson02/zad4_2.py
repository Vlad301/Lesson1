g = (int(input("Enter number: ")))
m = abs(g)
max = m % 10
while m >= 1:
    m = m // 10
    if m % 10 > max:
        max = m % 10
    if m > 9:
        continue
    else:
        print(f"Max number = {max} ")
        break
