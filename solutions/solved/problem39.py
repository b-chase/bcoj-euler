"""<p>If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a, b, c\}$, there are exactly three solutions for $p = 120$.</p>
<p>$\{20,48,52\}$, $\{24,45,51\}$, $\{30,40,50\}$</p>
<p>For which value of $p \le 1000$, is the number of solutions maximised?</p>

"""

import euler_math as em
from collections import defaultdict

def solve(debug=False):
    res=0
    
    max_p = 1000
    max_c = 1000 // 2  # true limit - triangle side can't be longer than other two combined
    max_a = 1000 // 4  # true limit - otherwise side 'b' is shorter than side 'a'
    # max_b = max_c - 1  # true limit - 'a' can be size of 1 but 'b' can't be larger than 'c'

    squares = [i**2 for i in range(0, max_c)]
    sq_set = set(squares)

    max_c2 = squares[-1]

    soln_cts = defaultdict(lambda: 0)

    for a in range(1,max_a):
        a2 = squares[a]

        max_b = (max_p - a) // 2 + 1
        for b in range(a+1, max_b):
            b2 = squares[b]

            max_c = 1000 - a - b
            c2 = a2 + b2

            if c2 > max_c2:
                break

            if c2 in sq_set:
                c = em.int_sqrt(a2+b2)
                # c = squares.index(c2)
                p = a + b + c
                soln_cts[p] += 1
    
    res = max(soln_cts.items(), key=lambda x: x[1])

    

    print(f"*** Answer: {res} ***")