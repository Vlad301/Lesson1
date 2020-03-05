# генератор count
from itertools import count

for el in count(0):
    if el > 15:
        break
    else:
        print(el)

# генератор cycle
from itertools import cycle

с = 0
for el in cycle("vlad"):
    if с > 10:
        break
    print(el)
    с += 1