import stock
import tableformat
p = stock.read_portfolio('Data/portfolio.csv')
tableformat.print_table(p, ['name', 'shares', 'price'])