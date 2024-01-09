# https://projecteuler.net/problem=85
"""<p>By counting carefully it can be seen that a rectangular grid measuring $3$ by $2$ contains eighteen rectangles:</p>
<div class="center">
<img src="resources/images/0085.png?1678992052" class="dark_img" alt=""></div>
<p>Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.</p>

"""

import euler_math as em
import numpy as np
from sympy.abc import y

def solve(debug=False):
    
    def count_rectangles(d:tuple[int]) -> int:
        # counts number of rectangles in a rectangle of dimensions d
        x, y = d
        x_ct = x*(x+1)//2
        y_ct = y*(y+1)//2
        return x_ct*y_ct
    
    closest = 0
    min_diff = 2_000_000
    n, m = 1, 1
    res = n*m

    for n in range(1,1000):
        for m in range(1,n+1):
            rect_count = count_rectangles((n,m))
            diff = abs(rect_count - 2_000_000)
            if diff < min_diff:
                min_diff = diff
                closest = rect_count
                res = n*m
                if debug:
                    print(f"Closest value of {closest} achieved at dimension d=({n}, {m})")
            elif rect_count > 2_000_000:
                # we've gone too far, so break out of the inner loop and move onto the next n
                # if debug:
                #     print(f"Breaking inner loop at value of {rect_count} with dimension d=({n}, {m})")
                break

    

    print(f'*** Answer: {res} ***')