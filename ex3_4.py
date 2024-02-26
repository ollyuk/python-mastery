import stock

row = ['a', 100, 22.32]

s = stock.DStock(*row)
stock.print_portfolio([s])
s.shares = -10
s.shares = '10'
print(s.cost)
