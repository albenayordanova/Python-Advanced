txt = input()
stock = {}
for el in txt:
    if el not in stock:
        stock[el] = 0
    stock[el] += 1
for k, v in sorted(stock.items()):
    print(f'{k}: {v} time/s')