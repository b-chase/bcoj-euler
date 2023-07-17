# https://projecteuler.net/problem=62
"""<p>The cube, $41063625$ ($345^3$), can be permuted to produce two other cubes: $56623104$ ($384^3$) and $66430125$ ($405^3$). In fact, $41063625$ is the smallest cube which has exactly three permutations of its digits which are also cube.</p>
<p>Find the smallest cube for which exactly five permutations of its digits are cube.</p>

"""
from collections import defaultdict
import euler_math as em
from solutions.euler_tools import permute_down, digits_to_num, get_digits

def solve(debug=False):

    cubic_permutations = 5

    cube_list = [x**3 for x in range(2, 10_000)]
    cube_set = set(cube_list)

    digit_families = defaultdict(lambda: [])

    for c in cube_list:
        c_digits = tuple(sorted(get_digits(c)))
        digit_families[c_digits].append(c)
        if debug:
            print(digit_families[c_digits])
        
        if len(digit_families[c_digits]) >= cubic_permutations:
            res = sorted(digit_families[c_digits])
            break


    print(f"*** Answer: {res} ***")