stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 64400, 'recomend': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000},
]

print(type(stock))
print(type(stock[0]))
print(type(stock[0]['recomend']))

stock[2]['stock'] += 9
print(stock[2]['stock'])
stock[0]['colors'] = 2
print(stock[0])
print(stock[0]['recomend'][1])
del stock[0]['recomend']
print(stock[0]) 