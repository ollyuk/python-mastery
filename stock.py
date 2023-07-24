class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        cost = self.shares * self.price
        return f'{cost:.2f}'
