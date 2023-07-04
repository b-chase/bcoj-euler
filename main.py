from solutions import problem1
from time import time_ns

start_ns = time_ns()

problem1.solve()

elapsed = (time_ns() - start_ns)/1e3
print(f'\nSolved in {elapsed:.5f} us')
