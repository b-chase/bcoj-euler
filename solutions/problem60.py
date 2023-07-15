# https://projecteuler.net/problem=60
"""<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>

"""

import euler_math.euler_math as em
# from solutions.euler_tools import get_digits
from collections import defaultdict

def solve(debug=False):
    
    res=None

    plist = em.get_primes(1_000_000)
    max_p = plist[-1]
    pset = set(plist)
    
    pairs = defaultdict(lambda: set())

    # check all primes (skipping '2')
    for p in plist[1:(max_p//10)]:
        ppot = len(str(p))
        for i in range(1,ppot):
            p_right = p % 10**i
            if p_right < 10**(i-1):
                continue
            p_left = p // 10**i

            rev = p_right * 10**(ppot-i) + p_left
            # print(p_left, p_right, rev)

            if p_right in pset and p_left in pset and rev in pset:
                pairs[p_left].add(p_right)
                pairs[p_right].add(p_left)

    def filter_overlapping(check_p_list, min_overlaps)
        for p1 in check_p_list:
            matches = pairs[p1]
            if len(matches) < min_overlaps-1:
                continue
            
            # each subset should overlap with the current one
            for m in matches:
                
    
    res = filter_overlapping(check_p_list=pairs.keys(), min_overlaps=5)
        
    print(f"*** Answer: {res} ***")