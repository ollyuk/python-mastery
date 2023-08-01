import readrides

# There are 4 columns of data.
# - route: Column 0.  The bus route name.
# - date: Column 1.  A date string of the form MM/DD/YYYY.
# - daytype: Column 2. A day type code (U=Sunday/Holiday, A=Saturday, W=Weekday)
# - rides: Column 3. Total number of riders (integer)



rows = readrides.read_rides_as_tuples('Data/ctabus.csv')
# return a set
print(f'Unique routes in Chicago {len({row for row in rows}):,}')