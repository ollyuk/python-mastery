import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = int(shares)
        self.price = float(price)

    def cost(self):
        cost = self.shares * self.price
        return f'{cost:.2f}'

    def sell(self, value):
        self.shares = self.shares - value
        return self.shares

    def __str__(self):
        # return f'{self.name=} {self.shares=} {self.price=}'
        return f'{self.name} {self.shares} {self.price}'


class Portfolio:
    def __init__(self, headers):
        self.headers = headers
        self.divider = ('------', '------', '------')
        self.portfolio = []

    def __add__(self, stock):
        self.portfolio.append(stock)

    def print_portfolio(self):
        print('%10s %10s %10s' % tuple(self.headers))
        print('%10s %10s %10s' % tuple(self.divider))
        for s in self.portfolio:
            print('%10s %10d %10.2f' % (s.name, s.shares, s.price))


def read_portfolio(filepath):
    with open(filepath) as f:
        rows = csv.reader(f)
        headers = next(rows)
        p = Portfolio(headers)
        for row in rows:
            p.portfolio.append(Stock(row[0], row[1], row[2]))
    return p
