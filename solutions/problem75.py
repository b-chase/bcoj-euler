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
    max_perimeter = 1_500_000

    # max_perimeter = 130

    squares = {x*x:x for x in range(max_perimeter//2)}

    seen_triangles = set()
    triples = Counter()

    for b in range(2, max_perimeter//2):
        if debug and b%1000==0:
            print(b)
        min_a = em.int_sqrt(2*b+1)
        for a in range(min_a, b):
            couplet = (a,b)
            if couplet in seen_triangles:
                continue
            c2 = a*a + b*b
            if c2 in squares:
                c = squares[c2]
                # if debug:
                #     print(f"{a}^2 + {b}^2 = {c}^2")
                perim = a+b+c
                i = 1
                while perim*i < max_perimeter:
                    triples[perim*i] += 1
                    new_couplet = (a*i, b*i)
                    seen_triangles.add(new_couplet)
                    i += 1
        
    res = sum(x for k,x in triples.items() if x==1 and k <= max_perimeter)
    
    if debug:
        for k,x in triples.items():
            print(f"Triangles with perimeter {k}: {x}")
    print(f"*** Answer: {res} ***")