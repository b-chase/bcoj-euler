"""
Takes CLI arguments 'problem_number' and 'microseconds' in that order and saves results
"""

from argparse import ArgumentParser
import pandas as pd
import os

ap = ArgumentParser()
ap.add_argument('problem_number', type=int, action='store')
ap.add_argument('microseconds', type=float, action='store')

args = vars(ap.parse_args())

solved_list_file = 'solutions/solved.txt'

solved_list = pd.read_csv(solved_list_file)
solved_list.loc[len(solved_list)] = [args['problem_number'], args['microseconds']]
solved_list.sort_values('problem_number')

print(solved_list)

solved_list.to_csv(solved_list_file,index=False)