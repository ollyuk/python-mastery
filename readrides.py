# todo: loop over the 4 different ways to read the data and display the results in a table

from collections import namedtuple
import csv
import time


# tuple
def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_namedtuple(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            # a name tuple
            Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
            record = Row(route=route, date=date, daytype=daytype, rides=rides)
            print(len(record))
        # records.append(record)
    return records


# A class with __slots__
class Row_slot:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


# a dictionary
def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records


# A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename, row_class):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = row_class(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc

    tracemalloc.start()
    start_time = time.time()
    # rows = read_rides_as_tuples('Data/ctabus.csv')
    # rows = read_rides_as_namedtuple('Data/ctabus.csv')
    # rows = read_rides_as_dict('Data/ctabus.csv')
    # rows = read_rides_as_class('Data/ctabus.csv', Row_slot)
    # rows = read_rides_as_class('Data/ctabus.csv', Row)
    current, peak = tracemalloc.get_traced_memory()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Memory Use: Current {current / (1024 * 1024):.2f}MB, Peak {peak / (1024 * 1024):.2f}MB')
    print(f'Elapsed Time: {elapsed_time:.2f}s')
