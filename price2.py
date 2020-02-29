def format_price(price):
    price = int(price)
    p = "Цена: " + str(price) + " руб."
    return p
print(format_price(56.24))