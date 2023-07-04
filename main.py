from time import monotonic_ns
from argparse import ArgumentParser
import os

ap = ArgumentParser()
ap.add_argument('problem', type=int)
pnum = vars(ap.parse_args())['problem']
pname = f'problem{pnum}'
problem = getattr(__import__('solutions', fromlist=[pname]), pname)

start_ns = monotonic_ns()
problem.solve()
elapsed = (monotonic_ns() - start_ns)/1e3

print(f'\nSolution in {elapsed:.6f} us')

is_correct = input('Solution correct? (y/n) ').lower() == 'y'

if is_correct:
    os.system(f'py -m save {pnum} {elapsed}')
    os.system('py -m next')
