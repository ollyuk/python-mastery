# making a parsing utility function
import csv

def read_csv_as_dicts(filepath, coltypes):
    f = open(filepath)
    rows = csv.reader(f)
    headers = next(rows)
    list_dicts = []
    for row in rows:
        list_dicts.append({name:func(val) for name, func, val in zip(headers, coltypes, row)})
    return list_dicts