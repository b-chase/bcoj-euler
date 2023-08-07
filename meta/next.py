import pandas as pd
from argparse import ArgumentParser
import requests
import os
import re


ap = ArgumentParser()

ap.add_argument('--problem_number', '-p', type=int, required=False)

args = vars(ap.parse_args())
cli_pno = args['problem_number']

def load_problem(pnum:int):
    problem_url = f"https://projecteuler.net/minimal={pnum}"
    problem_html = requests.get(url=problem_url).content.decode()
    try:
        prob_text_file = re.search(r'href\=\"(.+?txt)', problem_html)
        if prob_text_file:
            file_link = f"https://projecteuler.net/{prob_text_file.groups()[0]}"
            print(file_link)
            file_content = requests.get(file_link).content.decode()
            with open(f"solutions/problem{pnum}.txt", "x") as t:
                t.write(file_content)
        # raise Exception("Check for text file!")
        with open(f'solutions/problem{pnum}.py', 'x') as f:
            try:
                f.write(f"# https://projecteuler.net/problem={pnum}\n")
                f.write(f'''"""{problem_html}"""\n\n''')
                
            except Exception as e:
                f.write(f"# There was a problem loading the HTML for this problem\n\n")
                print(e)
            indent = "    "
            starting_code = [
                "import euler_math as em",
                "",
                "def solve(debug=False):",
                indent,
                indent+"res=None",
                indent,
                indent+"print(f'*** Answer: {res} ***')"
            ]
            if prob_text_file:
                starting_code.insert(4, indent+f"with open('solutions/problem{pnum}.txt') as f:\n"+2*indent+"pass\n"+indent)
            f.write('\n'.join(starting_code))
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