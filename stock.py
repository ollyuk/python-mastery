# stock.py
from decimal import Decimal


class Stock:
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        name, shares, price = [func(val) for func, val in zip(self._types, [name, shares, price])]
        self.name = name
        self._shares = shares
        self._price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        if value < 0:
            raise ValueError('Shares must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('Expected float')
        if value < 0:
            raise ValueError('Price must be >= 0')
        self._price = value

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


# new subclass that inherits from Stock class
class DStock(Stock):
    @property
    def cost(self):
        TWOPLACES = Decimal('0.01')
        return Decimal(self.shares * self.price).quantize(TWOPLACES)


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
            record = Stock.from_row((row[0], int(row[1]), float(row[2])))
            portfolio.append(record)
    return portfolio


# exercise C) modify to create objects using a class other than `Stock`
def read_portfolio_cust(filename, stock=Stock):
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = stock.from_row((row[0], row[1], row[2]))
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
