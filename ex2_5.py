import tracemalloc
import sys
from readrides import read_rides_as_columns
from pmutils import print_tracemem
print("Lists and memory usage")
i = []
print('list ()')
for n in range(1, 1000):
    i.append(1)
    if n%100 == 0:
        print(f'for {len(i)} items the size is {sys.getsizeof(i):,} bytes')

r = {'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
print(sys.getsizeof(r))
print('dict {}')
for n in range(1, 1000):
    r[str(n)] = 10
    if n%100 == 0:
        print(f'for {n} items the size is {sys.getsizeof(r):,} bytes')

r = {'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
print(sys.getsizeof(r))
nrows=577563
print(f'store nrows of data at 240bytes per row: {(nrows*240)/1048576:,.2f}')
print(f'store nrows of data in 4 lists as 8 bytes per element (32bytes a row): {(nrows*4*8)/1048576:,.2f}')


# from tracemem import TraceMem
# tracemalloc.start()
# cols = read_rides_as_columns('Data/ctabus.csv')
# t = TraceMem(tracemalloc.get_traced_memory())



tracemalloc.start()
cols = read_rides_as_columns('Data/ctabus.csv')
c,p =tracemalloc.get_traced_memory()
mb_val = 1048576
c = c / mb_val
p= p/ mb_val
print(f'{c:,.2f}, {p:,.2f}')
