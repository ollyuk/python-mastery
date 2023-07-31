import csv
from collections import Counter


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # grab first line as column headings
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio('Data/portfolio.csv')

print('holidings > 100 shares')
print([s for s in portfolio if s['shares'] > 100])

print('total value of all shares')
print(sum(s['shares'] * s['price'] for s in portfolio))

print('all unique stock names')
print({s['name'] for s in portfolio})

print('all holdings')
print([s['name'] for s in portfolio])

print('Count the total shares of each stock')
total = {s['name']: 0 for s in portfolio}
for s in portfolio:
    total[s['name']] += s['shares']

print(total)


totals = Counter()
for s in portfolio:
    totals[s['name']] += s['shares']

print(totals)

