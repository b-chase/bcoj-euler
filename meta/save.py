"""
Takes CLI arguments 'problem_number' and 'microseconds' in that order and saves results
"""

from argparse import ArgumentParser
import pandas as pd
import os
import time

ap = ArgumentParser()
ap.add_argument('problem_number', type=int, action='store')
ap.add_argument('--microseconds', type=float, action='store', required=False, default=None)

args = vars(ap.parse_args())
pnum = args['problem_number']

if args['microseconds'] in args:
    solved_list_file = 'solutions/solved_list.txt'
    solved_list = pd.read_csv(solved_list_file)
    solved_list.loc[len(solved_list)] = [pnum, args['microseconds'], time.ctime()]
    solved_list.sort_values('problem_number')
    print(solved_list)
    solved_list.to_csv(solved_list_file,index=False)


problem_file = f'solutions/problem{pnum}.py'
save_range_start = 1 + 20 * ((pnum-1) // 20)
save_range = (save_range_start, save_range_start+19)
save_folder = f'solutions/solved/{save_range[0]} to {save_range[1]}'
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

os.rename(problem_file, f'{save_folder}/problem{pnum}.py')

problem_text = f'solutions/problem{pnum}.txt'
if os.path.exists(problem_text):
    os.rename(problem_text, f'{save_folder}/problem{pnum}.txt')

