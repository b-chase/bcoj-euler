"""<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
<p>What is the $10\,001$st prime number?</p>

"""

import euler_math as em
from math import log

def solve(debug=False):
    nth_p = 10001
    
    plist = em.get_primes(int(nth_p * log(nth_p) + 1e6))
    if len(plist) >= nth_p:
        print(plist[nth_p-1])
    else:
        raise ValueError(f"Didn't generate enough primes! ({len(plist)})")