# https://projecteuler.net/problem=69
"""<p>Euler's totient function, $\phi(n)$ [sometimes called the phi function], is defined as the number of positive integers not exceeding $n$ which are relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$, are all less than or equal to nine and relatively prime to nine, $\phi(9)=6$.</p>
<p>It can be seen that $n = 6$ produces a maximum $n/\phi(n)$ for $n\leq 10$.</p>
<p>Find the value of $n\leq 1\,000\,000$ for which $n/\phi(n)$ is a maximum.</p>

"""

import euler_math as em
from sympy.ntheory import totient

def solve(debug=False):
    
    res=None
    big = 0
    for n in range(2, 1_000_001):
        tn = em.totient(n)
        
        # if debug:
        #     print(f"t{n} = {tn}")
        
        if totient(n) != tn:
            print(f"Incorrect value for {n}:")
            print(f"Expected to get {totient(n)}, yielded {tn}")
            raise AssertionError
        
        if n / tn > big:
            big = (n / tn)
            res = n
            
            if debug:
                print(f"{n}/{tn} ~= {big:.3f}")
                
    
    
    print(f"*** Answer: {res} ***")