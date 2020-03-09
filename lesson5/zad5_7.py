import json
pribyl = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('zad5_7.txt', 'r') as file:
    for line in file:
        name, firm, dox, izder = line.split()
        pribyl[name] = int(dox) - int(izder)
        if pribyl.setdefault(name) >= 0:
            prof = prof + pribyl.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    pribyl.update(pr)
    print(f'Прибыль каждой компании - {pribyl}')

with open('zad5_7.json', 'w') as write_js:
    json.dump(pribyl, write_js)

    js_str = json.dumps(pribyl)
    print(f'json: \n '
          f' {js_str}')