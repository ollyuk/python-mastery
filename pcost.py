import stock


def portfolio_cost(filename):
    running_total = 0.0
    with open(f'{filename}') as f:
        for line in f:
            name, quant, price = line.split()
            try:
                running_total += int(quant) * float(price)
            except ValueError as e:
                print("Couldn't pass", repr(line))
                print('Reason:', e)

    return f'${running_total}'


def portfolio(filename):
    with open(f'{filename}') as f:
        for line in f:
            name, quant, price = line.split()
            try:
                s = stock.Stock(name, int(quant), float(price))
            except Exception as e:
                print(e)
                s = stock.Stock('error', 0, 0)
            print(f'{s.name}, cost: ${s.cost()}')


if __name__ == '__main__':
    print(portfolio('Data/portfolio.dat'))
    print(portfolio_cost('Data/portfolio.dat'))
