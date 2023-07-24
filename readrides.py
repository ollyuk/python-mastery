import csv


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


if __name__ == '__main__':
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    current, peak = tracemalloc.get_traced_memory()
    # print(f'Memory Use: Current {current }mb, Peak {peak}mb')
    print(f'Memory Use: Current {current /(1024*1024)}MB, Peak {peak / (1024*1024)}MB')