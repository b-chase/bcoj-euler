"""<p>There are exactly ten ways of selecting three from five, 12345:</p>
<p class="center">123, 124, 125, 134, 135, 145, 234, 235, 245, and 345</p>
<p>In combinatorics, we use the notation, $\displaystyle \binom 5 3 = 10$.</p>
<p>In general, $\displaystyle \binom n r = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times ... \times 3 \times 2 \times 1$, and $0! = 1$.
</p>
<p>It is not until $n = 23$, that a value exceeds one-million: $\displaystyle \binom {23} {10} = 1144066$.</p>
<p>How many, not necessarily distinct, values of $\displaystyle \binom n r$ for $1 \le n \le 100$, are greater than one-million?</p>
"""

import euler_math as em
from math import comb

def solve(debug=False):
    
    res=0

    # comb(N, i) == comb(N, N-i)

    for n in range(1,101):
        for i in range(1, n-1):
            c = comb(n, i)
            if c > 1e6:
                if debug:
                    print(n, i, c)
                # passing = n - 2*(i-1)
                # print(n, i, passing)
                res += 1
                # break



    
    print(f"*** Answer: {res} ***")