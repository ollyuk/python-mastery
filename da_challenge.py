import readrides
from collections import Counter

# There are 4 columns of data.
# - route: Column 0.  The bus route name.
# - date: Column 1.  A date string of the form MM/DD/YYYY.
# - daytype: Column 2. A day type code (U=Sunday/Holiday, A=Saturday, W=Weekday)
# - rides: Column 3. Total number of riders (integer)


rows = readrides.read_rides_as_tuples('Data/ctabus.csv')
# return a set
print(f'Unique routes in Chicago {len({route[0] for route in rows}):,}')

travel_date = '02/02/2011'
date2_2_01 = [row for row in rows if row[1] == travel_date]
print(f'Passengers on route 2, {travel_date} - {sum([pas[3] for pas in date2_2_01 if pas[0] == "22"])}')


rides_per_route = Counter()
for row in rows:
    rides_per_route[row[0]] += int(row[3])

for route, count in rides_per_route.most_common():
    print('%5s %10d' % (route, count))


# all the data for the 2001 grouped by route
date2001 = [(row[0], row[3]) for row in rows if '/2001' in row[1]]
totals2001 = Counter()
for route in date2001:
    totals2001[route[0]] += int(route[1])
# print((totals2001))

date2011 = [(row[0], row[3]) for row in rows if '/2011' in row[1]]
totals2011 = Counter()
for route in date2011:
    totals2011[route[0]] += int(route[1])
# print((totals2011))

# show the difference between each dict item..
diff = {}
for route, passengers in totals2011.items():
    if route in totals2001:
        diff[route] = totals2011[route] - totals2001[route]
# print(diff)

diff_c= Counter(diff)
print('Biggest increase from 2001 - 2011')
print(diff_c.most_common(5))
