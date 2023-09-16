def print_table(data, headers):
    print('%10s' * len(headers) % tuple(key for key in headers))
    print(('-'*10 + ' ')* len(headers))
    for item in data:
        print('%10s' * len(headers) % tuple(getattr(item, h) for h in headers))