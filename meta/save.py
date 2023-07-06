"""
Takes CLI arguments 'problem_number' and 'microseconds' in that order and saves results
"""

from argparse import ArgumentParser
import pandas as pd
import os
import time

ap = ArgumentParser()
ap.add_argument('problem_number', type=int, action='store')
ap.add_argument('microseconds', type=float, action='store')

args = vars(ap.parse_args())
pnum = args['problem_number']

solved_list_file = 'solutions/solved_list.txt'

solved_list = pd.read_csv(solved_list_file)
solved_list.loc[len(solved_list)] = [pnum, args['microseconds'], time.ctime()]
solved_list.sort_values('problem_number')

print(solved_list)

solved_list.to_csv(solved_list_file,index=False)


problem_file = f'solutions/problem{pnum}.py'
os.rename(problem_file, f'solutions/solved/problem{pnum}.py')

