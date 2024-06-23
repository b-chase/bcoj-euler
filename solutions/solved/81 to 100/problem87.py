# https://projecteuler.net/problem=87
"""<p>The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is $28$. In fact, there are exactly four numbers below fifty that can be expressed in such a way:</p>
\begin{align}
28 &amp;= 2^2 + 2^3 + 2^4\\
33 &amp;= 3^2 + 2^3 + 2^4\\
49 &amp;= 5^2 + 2^3 + 2^4\\
47 &amp;= 2^2 + 3^3 + 2^4
\end{align}
<p>How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?</p>

"""

import euler_math as em
from math import sqrt

class Prime(int):
    # class extending integers to include squares, cubes, and quartics as properties
    @property
    def square(self):
        return int(self)**2
    
    @property
    def cube(self):
        return int(self)**3
    
    @property
    def tesseract(self):
        return int(self)**4
    

def solve(debug=False):
    
    upper_limit = 50_000_000
    
    prime_limit = int(sqrt(upper_limit))+1
    # p3_limit = int(sqrt(prime_limit))+1
    # p2_limit = int(upper_limit**0.33)+1
    
    prime_list = [Prime(x) for x in em.get_primes(prime_limit)]
    sum_res = set()
    
    for p1 in prime_list:
        assert p1 <= prime_limit
        
        for p2 in prime_list:
            rem2 = upper_limit - p1.square - p2.cube
            if rem2 <= 0:
                break
            
            for p3 in prime_list:
                s = p1.square + p2.cube + p3.tesseract
                if s <= upper_limit:
                    # print(f"{p1}^2 + {p2}^3 + {p3}^4 = {s}")
                    sum_res.add(s)
                else:
                    break
    
    
    res=len(sum_res)
    
    print(f'*** Answer: {res} ***')