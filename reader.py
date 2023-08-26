# making a parsing utility function
import csv
import tracemalloc
import collections


def read_csv_as_dicts(filepath, coltypes):
    f = open(filepath)
    rows = csv.reader(f)
    headers = next(rows)
    list_dicts = []
    for row in rows:
        list_dicts.append({name: func(val) for name, func, val in zip(headers, coltypes, row)})
    return list_dicts


def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = RideData()
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


class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        print(index)
        # slice(1, 2, None)
        if isinstance(index, slice):
            ret_val = []
            for n in range(index.start, index.stop + 1):
                ret_val.append(
                    {'route': self.routes[n],
                     'date': self.dates[n],
                     'daytype': self.daytypes[n],
                     'rides': self.numrides[n]}
                )
        else:
            ret_val = {'route': self.routes[index],
                       'date': self.dates[index],
                       'daytype': self.daytypes[index],
                       'rides': self.numrides[index]}
        return ret_val

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


def get_formatted_traced_memory():
    memory_stats = tracemalloc.get_traced_memory()
    current, peak = memory_stats

    formatted_memory_stats = (
        f"Current Memory Usage: {current / (1024 * 1024):.2f} MB\n"
        f"Peak Memory Usage: {peak / (1024 * 1024):.2f} MB"
    )

    return formatted_memory_stats
