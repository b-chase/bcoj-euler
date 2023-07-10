"""<p>The arithmetic sequence, $1487, 4817, 8147$, in which each of the terms increases by $3330$, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the $4$-digit numbers are permutations of one another.</p>
<p>There are no arithmetic sequences made up of three $1$-, $2$-, or $3$-digit primes, exhibiting this property, but there is one other $4$-digit increasing sequence.</p>
<p>What $12$-digit number do you form by concatenating the three terms in this sequence?</p>

"""

import euler_math as em
from solutions.euler_tools import permute_down

def solve(debug=False):
    plist = [x for x in em.get_primes(10000) if x > 1000]
    pset = set(plist)

    res=None

    ans = []
    for p in plist[::-1]:
        digits = list(str(p))
        permuted_primes = []
        while permute_down(digits):
            new_p = int(''.join(digits))
            if new_p in pset:
                permuted_primes.append(new_p)

        if len(permuted_primes) >= 3:
            if debug:
                print(permuted_primes)
            for np in permuted_primes:
                diff = p - np
                nnp = np - diff
                if diff > 0 and nnp in permuted_primes:
                    ans.append((nnp, np, p))

    res = ans

    
    print(f"*** Answer: {res} ***")