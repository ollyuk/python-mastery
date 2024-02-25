# from our stock module import the class Stock to the local scope.
from stock import Stock

row = ['AA', '100', '22.22']

# now we can use in local scope and create our new stock instance.
s = Stock.from_row(row)

print(f'{s.name=}, {s.price=} * {s.shares=}={s.cost()}')