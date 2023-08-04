# https://projecteuler.net/problem=71
"""<p>Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive integers. If $n \lt d$ and $\operatorname{HCF}(n,d)=1$, it is called a reduced proper fraction.</p>
<p>If we list the set of reduced proper fractions for $d \le 8$ in ascending order of size, we get:
$$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7, \frac 1 3, \frac 3 8, \mathbf{\frac 2 5}, \frac 3 7, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7, \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8$$</p>
<p>It can be seen that $\dfrac 2 5$ is the fraction immediately to the left of $\dfrac 3 7$.</p>
<p>By listing the set of reduced proper fractions for $d \le 1\,000\,000$ in ascending order of size, find the numerator of the fraction immediately to the left of $\dfrac 3 7$.</p>

"""

import euler_math as em

def solve(debug=False):
    res = em.Fraction(0, 1)
    x = em.Fraction(3, 7)
    z = em.Fraction(300_000, 700_001)
    assert z < x

    while z.denominator <= 1_000_000:
        if z < x:
            if z > res:
                res = em.Fraction(z.numerator, z.denominator)
                if debug:
                    print(f"{res}  <  {x}")
            z.numerator += 1
        else:
            z.denominator += 1

    
    print(f"*** Answer: {res} ***")