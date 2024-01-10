# https://projecteuler.net/problem=86
"""<p>A spider, S, sits in one corner of a cuboid room, measuring $6$ by $5$ by $3$, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is $10$ and the path is shown on the diagram.</p>
<div class="center">
<img src="resources/images/0086.png?1678992052" class="dark_img" alt=""><br></div>
<p>However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.</p>
<p>It can be shown that there are exactly $2060$ distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of $M$ by $M$ by $M$, for which the shortest route has integer length when $M = 100$. This is the least value of $M$ for which the number of solutions first exceeds two thousand; the number of solutions when $M = 99$ is $1975$.</p>
<p>Find the least value of $M$ such that the number of solutions first exceeds one million.</p>

"""

import euler_math as em
from math import sqrt

def solve(debug=False):
    
    
    
    # largest side of cuboid allowed
    max_m = 2000
    squares = [i**2 for i in range(0, 2*max_m+2)]
    sq_set = set(squares)
    
    # largest perimeter of produced pythagorean triangle
    max_p = 10 * max_m
    max_c = max_m // 2  # true limit - triangle side can't be longer than other two combined
    max_a = max_m // 4  # true limit - otherwise side 'b' is shorter than side 'a'
    
    max_c2 = squares[-1]
    
    triples = {}
    # build list of integer triples
    for a in range(1, max_a):
        a2 = squares[a]
        max_b = (max_p - a) // 2 + 1  # should be larger than side 'a'
        for b in range(a+1, max_b):
            b2 = squares[b]
            # max_c = 1000 - a - b
            c2 = a2 + b2

            if c2 > max_c2:
                break

            if c2 in sq_set:
                c = sqrt(c2)
                triples[(a,b)] = c
    
    # now we've identified triples, we can determine cuboids
    triples_counter = [0]*(max_m+1)
    for i in range(1, max_m+1):
        for j in range(1, i+1):
            for k in range(1, j+1):
                a, b = i, j+k
                a, b = min(a,b), max(a,b)
                if (a,b) in triples:
                    c = triples[(a,b)]
                    triples_counter[i] += 1
                    # print(i, j, k)

        if triples_counter[i] > 10:
            print(f"At max_m of {i} we have {triples_counter[i]} distinct cuboids")
    
    res = None  
    
    print(f'*** Answer: {res} ***')