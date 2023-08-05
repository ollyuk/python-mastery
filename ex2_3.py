# import csv
# from pprint import pprint
# from collections import defaultdict
#
# f = open('Data/portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# print(headers)
# rows = list(f_csv)
#
#
# byname = defaultdict(list)
# for name, *data in rows:
#     byname[name].append(data)
#
#
import csv
# if __name__ == '__main__':
# nums = list(i for i in range(1, 101))
# squares = (x * x for x in nums)
# for n in squares:
#     print(n)
#
#
# def cubes(nums):
#     for x in nums:
#         yield x*x*x
#
# for n in cubes(nums):
#     print(n)


# from readport import read_portfolio
#
# portfolio = read_portfolio('Data/portfolio.csv')
# print(sum(s['shares']*s['price'] for s in portfolio))
#
# print(min(s['shares'] for s in portfolio))
#
# print(any(s['name'] =='IBM' for s in portfolio))
#
# print(all(s['name'] =='IBM' for s in portfolio))
#
# print(sum(s['shares'] for s in portfolio if s['name']=='IBM'))
#
# s = ('GOOG',100,490.10)
# # 's'.join(s)
#
# print(','.join(str(x) for x in s))

# which day has the most passengers for route 22
import tracemalloc

tracemalloc.start()
import readrides

rows = readrides.read_rides_as_dict('Data/ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
print(max(rt22, key=lambda row: row['rides']))
current, peak = tracemalloc.get_traced_memory()
print(f'Memory Use: Current {current / (1024 * 1024):.2f}MB, Peak {peak / (1024 * 1024):.2f}MB')

import tracemalloc

tracemalloc.start()
f = open('Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers,row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(max(rt22, key=lambda row: int(row['rides'])))
current, peak = tracemalloc.get_traced_memory()
print(f'Memory Use: Current {current / (1024 * 1024):.2f}MB, Peak {peak / (1024 * 1024):.2f}MB')
