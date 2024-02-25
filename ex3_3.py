# from our stock module import the class Stock to the local scope.
from stock import Stock
from stock import DStock

row = ['AA', '100', '32.20']

# now we can use in local scope and create our new stock instance.
s = Stock.from_row(row)

print(f'{s.name=}, {s.price=} * {s.shares=}={s.cost()}')

sd = DStock.from_row(row)
print(f'{sd.name=}, {sd.price=} * {sd.shares=}={sd.cost()}')
