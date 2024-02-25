# from our stock module import the class Stock to the local scope.
from stock import Stock
from stock import DStock
import stock
from reader import read_csv_as_instances

row = ['AA', '100', '32.20']

# now we can use in local scope and create our new stock instance.
s = Stock.from_row(row)

print(f'{s.name=}, {s.price=} * {s.shares=}={s.cost()}')

sd = DStock.from_row(row)
print(f'{sd.name=}, {sd.price=} * {sd.shares=}={sd.cost()}')


pf = stock.read_portfolio_cust('Data/portfolio.csv', DStock)
stock.print_portfolio(pf)

# create a list stocks by specifying the source and Stock class to use.
portfolio = read_csv_as_instances('Data/portfolio.csv', DStock)
stock.print_portfolio(portfolio)