"""<p>By replacing the 1<sup>st</sup> digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.</p>
<p>By replacing the 3<sup>rd</sup> and 4<sup>th</sup> digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.</p>
<p>Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.</p>

"""

import euler_math as em
from solutions.euler_tools import get_digits, digits_to_num
from collections import defaultdict


def sub_combos(seq:list) -> list[list]:
    # permutes through the given sequence, returning all sub-combinations
    if len(seq)==1:
        return [seq]
    output = [[seq[0]]]
    for sub in sub_combos(seq[1:]):
        output.append([seq[0], *sub])
        if sub:
            output.append(sub)
    return output

def solve(debug=False):
    plist = em.get_primes(1000_000)
    pset = set(plist)

    res=None

    p_count = 0

    for p in plist:
        digits = get_digits(p)

        places = defaultdict(lambda: [])
        for i, d in enumerate(digits[:-1]):
            places[d].append(i)

        for d, places in places.items():
            combos = sub_combos(places)
            for perm in combos:
                ct = 0
                matching_p = []
                min_digit = 0 if perm[0] != 0 else 1
                for x in range(min_digit, 10):
                    new_digits = [x if j in perm else d for j, d in enumerate(digits)]
                    n = digits_to_num(new_digits)
                    if n in pset:
                        ct += 1
                        matching_p.append(n)
            
                if ct > p_count:
                    p_count = ct
                    
                    if debug:
                        print(p_count, matching_p)

                    



        
        

    print(f"*** Answer: {res} ***")