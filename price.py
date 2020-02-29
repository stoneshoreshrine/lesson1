def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Максимальная скидка равна 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

product = {"name": "Nokia 3310", "price": 3500, "dc": 17}
product["discounted_price"] = discounted(product["price"], product["dc"])
print(product)
print(discounted(100, 44))


#def get_summ(one, two, delimiter='&'):  Задание 1
   # one = str(one)
   # two = str(two)
   # delimiter = str(delimiter)
   # p = one + delimiter + two
   # return p
#print(get_summ("learn", "python").upper())