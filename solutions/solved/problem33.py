"""<p>The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the $9$s.</p>
<p>We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.</p>
<p>There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.</p>
<p>If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</p>

"""

import euler_math as em
from math import prod

def solve(debug=False):
    
    pairs = []
    
    for x in range(1,10):
        # number to be cancelled out
        nums = [(10*i + x, i) for i in range(1,10)]
        nums.extend([(10*x + i, i) for i in range(1,10)])
        
        for numer in nums:
            reduce_n = numer[1]
            for denom in [d for d in nums if d[0] > numer[0]]:
                reduce_d = denom[1]
                if denom[0] / numer[0] == denom[1] / numer[1]:
                    pairs.append((numer[0], denom[0]))
                    
                    if debug:
                        print((numer[0], denom[0]))

    
    np, dp = (prod(p[0] for p in pairs), prod(p[1] for p in pairs))
    
    res = dp / em.gcd(np, dp)
    
    
    print(res)
    
    pass