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
from collections import Counter


def solve(debug=False):
    max_perimeter = 1_500_00

    # max_perimeter = 130
    sqrts = dict()
    squares = []

    for x in range(0, max_perimeter//2 + 1):
        x2 = x * x
        sqrts[x2] = x
        squares.append(x2)

    max_c = 1+max_perimeter//2
    triples = Counter()
    
    def count_triples():
        return sum(ct for _,ct in triples.items() if ct == 1)

    min_a = 2
    b = 1
    for b2 in squares[2:]:
        b += 1
        min_a2 = 2*b+1

        while squares[min_a] < min_a2:
            min_a += 1
        
        a = min_a-1
        for a2 in squares[min_a:]:
            a += 1
            c2 = b2 + a2
            
            if c2 in sqrts:
                c = sqrts[c2]
                perim = a + b + c
                triples[perim] += 1

        if debug and b % 10000 == 0:
            print(f"B={b}, min_A={min_a}  >>  Triples up to {count_triples()}")
        

    
    res = sum(x for k,x in triples.items() if x==1 and k <= max_perimeter)
    
    if debug:
        for k,x in triples.items():
            print(f"Triangles with perimeter {k}: {x}")
    print(f"*** Answer: {res} ***")