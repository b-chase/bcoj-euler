# https://projecteuler.net/problem=80
"""<p>It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.</p>
<p>The square root of two is $1.41421356237309504880\cdots$, and the digital sum of the first one hundred decimal digits is $475$.</p>
<p>For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.</p>

"""

import euler_math as em
from euler_tools.math import frac_from_seq

def solve(debug=False):
    
    squares = set([x*x for x in range(1,101)])
    
    def digits_sum(n, root_terms=200):    
        res = em.root_cont_fraction(n, root_terms)
        frac = frac_from_seq(res)
        # print(frac)
        return sum(em.long_divide(frac[0], frac[1], 100)[:100])
    
    # trying to find minimum terms needed
    # for x in range(2, 10000):
    #     sums = [digits_sum(x, t_ct) for t_ct in [100, 175, 500, 1000]]
        
    #     print(f"sqrt({x}) digits sum to... {sums}")
        
    #     assert sums[1] == sums[-1]
    
    res = 0
    
    for z in range(1,101):
        if z in squares:
            continue
        sum_z = digits_sum(z)
        res += sum_z
    
    print(f"*** Answer: {res} ***")