g = int(input("Seconds: "))
chas = 3600
minuta = 60
a = g // chas
b = (g - (a * chas)) // minuta
c = g % minuta
if a <= 9 and b <= 9 and c <= 9:
    print(f"0{a}:0{b}:0{c}")
elif a <= 9 and b <= 9:
    print(f"0{a}:0{b}:{c}")
elif a <= 9:
    print(f"0{a}:{b}:{c}")
elif b <= 9:
    print(f"{a}:0{b}:{c}")
elif c <= 9:
    print(f"{a}:{b}:0{c}")
