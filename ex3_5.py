import stock, reader, tableformat


# read in the CSV file and pass the class we want it to use
portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.DStock)
# choose the formatter to use
formatter = tableformat.TextTableFormatter()
# print using that formatter
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
print('---')
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)

print('---')
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)