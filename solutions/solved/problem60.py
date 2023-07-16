# https://projecteuler.net/problem=60
"""<p>The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
<p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.</p>

"""

import euler_math.euler_math as em
# from solutions.euler_tools import get_digits
from collections import defaultdict

def solve(debug=False):
    
    res=None

    plist = em.get_primes(int(10**8))
    max_p = plist[-1]
    pset = set(plist)
    
    if debug:
        print("Primes Loaded")
    
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

    if debug:
        print("All pairs found")

    def find_overlaps(valid_primes: set[int], total_ct: int) -> list[set[int]]:
        
        if total_ct==1:
            return list(set([p]) for p in valid_primes)
        
        total = []
        for p1 in valid_primes:
            p1_pairs = pairs[p1].intersection(valid_primes)
            
            p1_sets = find_overlaps(p1_pairs, total_ct-1)
            base_set = set([p1])
            p1_out = [base_set.union(x) for x in p1_sets]
            
            total.extend(p1_out)
        
        return total
    
    all_sets = find_overlaps(pset, 5)
    
    smallest = float('Inf')
    for set_p in all_sets:
        sum_p = sum(set_p)
        if sum_p < smallest:
            smallest = sum_p
            res = [sum_p, set_p]
    
    
    
    print(f"*** Answer: {res} ***")