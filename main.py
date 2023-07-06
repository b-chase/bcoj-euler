from time import monotonic_ns
from argparse import ArgumentParser
import os

ap = ArgumentParser()
ap.add_argument('problem', type=int)
ap.add_argument('--debug', '-d', action='store_const', default=False, const=True)

cli_args = vars(ap.parse_args())
pnum = cli_args['problem']
debug = cli_args['debug']

pname = f'problem{pnum}'
problem = getattr(__import__('solutions', fromlist=[pname]), pname)

start_ns = monotonic_ns()
problem.solve(debug)
elapsed = (monotonic_ns() - start_ns)/1e3

print(f'\nSolution in {elapsed:.6f} us')

is_correct = input('Solution correct? (y/n) ').lower() == 'y'

if is_correct:
    os.system(f'py -m meta.save {pnum} {elapsed}')
    os.system('py -m meta.next')
    
