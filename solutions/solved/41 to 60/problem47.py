"""<p>The first two consecutive numbers to have two distinct prime factors are:</p>
\begin{align}
14 &amp;= 2 \times 7\\
15 &amp;= 3 \times 5.
\end{align}
<p>The first three consecutive numbers to have three distinct prime factors are:</p>
\begin{align}
644 &amp;= 2^2 \times 7 \times 23\\
645 &amp;= 3 \times 5 \times 43\\
646 &amp;= 2 \times 17 \times 19.
\end{align}
<p>Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?</p>

"""

import euler_math as em

def solve(debug=False):
    # pset = set(em.get_primes(1_000_000_000))

    res=None
    
    N = 4
    x = 2

    nums = []

    for x in range(1000000):
        f = em.prime_factors(x)
        if len(f) == N:
            nums.append(x)
        else:
            nums = []
        
        if len(nums) == N:
            res = nums[0]
            break



    print(f"*** Answer: {res} ***")