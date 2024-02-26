import stock

row = ['a', 100, 22.32]

s = stock.DStock(*row)
stock.print_portfolio([s])
print(s.cost)