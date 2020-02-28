items = int(input("Введите количество товара: "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= items:
    my_dict = dict({'название': input("Введите название: "), 'цена': input("Введите цену: "),
                    'количество': input('Введите количество: '), 'eд': input("Введите единицу измерения: ")})
    print("--------------")
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print("-" * 40)
print(my_analys)