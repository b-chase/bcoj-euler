import pandas as pd
from argparse import ArgumentParser
import requests
import os


ap = ArgumentParser()

ap.add_argument('--problem_number', '-p', type=int, required=False)

args = vars(ap.parse_args())
cli_pno = args['problem_number']

def load_problem(pnum:int):
    problem_url = f"https://projecteuler.net/minimal={pnum}"
    problem_html = requests.get(url=problem_url).content
    try:
        with open(f'solutions/problem{pnum}.py', 'x') as f:
            f.write(f'''"""{problem_html.decode()}"""\n\n''')
            f.write('''import euler_math as em\n\ndef solve(debug=False):\n    \n    res=0\n    \n    print(f"*** Answer: {res} ***")''')
    except FileExistsError:
        print("The specified problem file already exists!")
    os.system(f"code solutions/problem{pnum}.py -r")

if cli_pno:
    print(f"Loading problem # {cli_pno}")
    load_problem(cli_pno)
    quit()
else:
    print("Loading next unsolved problem based on results in 'solutions/solved.txt'")

solved_df = pd.read_csv('solutions/solved_list.txt')

solved_pnos = set(solved_df['problem_number'].values)

pno = 1

while pno <= len(solved_pnos):
    if pno in solved_pnos:
        pno += 1
    else:
        break

print(f'Loading problem: # {pno}')
load_problem(pno)