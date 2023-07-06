"""<p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$</p>
<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p>

"""

import euler_math as em
from math import sqrt

def solve(debug=False):
    # 1000//(sqrt(2)+2) ~= 293
    for a in range(1,500):
        # b**2 = (1000-a-b)**2 - a**2
        for b in range(1,a):
            c = 1000 - a - b
            c2 = c ** 2
            try_c2 = a**2 + b**2
            
            if c2 == try_c2:
                print(f'a*b*c: {a}*{b}*{c}={a*b*c}')
                return

            