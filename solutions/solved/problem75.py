# https://projecteuler.net/problem=75
"""<p>It turns out that $\pu{12 cm}$ is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.</p>
<ul style="list-style-type:none;">
<li>$\pu{\mathbf{12} \mathbf{cm}}$: $(3,4,5)$</li>
<li>$\pu{\mathbf{24} \mathbf{cm}}$: $(6,8,10)$</li>
<li>$\pu{\mathbf{30} \mathbf{cm}}$: $(5,12,13)$</li>
<li>$\pu{\mathbf{36} \mathbf{cm}}$: $(9,12,15)$</li>
<li>$\pu{\mathbf{40} \mathbf{cm}}$: $(8,15,17)$</li>
<li>$\pu{\mathbf{48} \mathbf{cm}}$: $(12,16,20)$</li></ul>
<p>In contrast, some lengths of wire, like $\pu{20 cm}$, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using $\pu{120 cm}$ it is possible to form exactly three different integer sided right angle triangles.</p>
<ul style="list-style-type:none;">
<li>$\pu{\mathbf{120} \mathbf{cm}}$: $(30,40,50)$, $(20,48,52)$, $(24,45,51)$</li></ul>

<p>Given that $L$ is the length of the wire, for how many values of $L \le 1\,500\,000$ can exactly one integer sided right angle triangle be formed?</p>

"""

import euler_math as em
from collections import defaultdict


def solve(debug=False):
    max_perimeter = 1_500_000
    # max_perimeter = 130

    couplets = set()
    triples = defaultdict(lambda: 0)
    
    def triple_counts(exact_count=1):
        return sum(1 for _, x in triples.items() if x==1)

    max_c = (max_perimeter//2) + (max_perimeter & 1)
    # max_b = max_c - 1
    max_m = em.int_sqrt(max_c)+1

    for m in range(2,max_m):
        m2 = m*m
        for n in range(1, m):
            n2 = n*n

            a = m2 - n2
            b = 2*m*n
            a, b = min(a,b), max(a,b)
            c = m2 + n2

            p = a+b+c
            
            for k in range(1, 1+max_perimeter//p):
                ma, mb, mc = a*k, b*k, c*k
                mp = ma+mb+mc
                if (ma,mb) not in couplets:
                    triples[mp] += 1
                    couplets.add((ma,mb))
                #     if debug:
                #         print(f"Found triangle {ma} + {mb} + {mc} = {mp}")
                # elif debug:
                #     print(f"Couplet already used: {ma} + {mb} + {mc} = {mp}")
            
        if debug and m % 100 == 0:
            print(f"Up to m={m}, triple count: {triple_counts(1)}")

    res = triple_counts(1)
    
    if debug:
        for k,x in triples.items():
            if x == 1:
                print(f"Triangles with perimeter {k}: {x}")
    print(f"*** Answer: {res} ***")