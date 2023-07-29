import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # grab first line as column headings
        for row in rows:
            record = {
                'name': row[0],
                'shares': row[1],
                'price': row[2]
            }
            portfolio.append(record)
    return portfolio
