# stock.py
from decimal import Decimal
class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# new subclass that inherits from Stock class
class DStock(Stock):
    types = (str, int, Decimal)

def read_portfolio(filename):
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(record)
    return portfolio


# exercise C) modify to create objects using a class other than `Stock`
def read_portfolio_cust(filename, class_type):
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = class_type(row[0], int(row[1]), float(row[2]))
            portfolio.append(record)
    return portfolio


def print_portfolio(portfolio):
    '''
    Make a nicely formatted table showing stock data
    '''
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-' * 10 + ' ') * 3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print_portfolio(portfolio)
