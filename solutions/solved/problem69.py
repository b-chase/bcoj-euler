# https://projecteuler.net/problem=69
"""<p>Euler's totient function, $\phi(n)$ [sometimes called the phi function], is defined as the number of positive integers not exceeding $n$ which are relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$, are all less than or equal to nine and relatively prime to nine, $\phi(9)=6$.</p>
<p>It can be seen that $n = 6$ produces a maximum $n/\phi(n)$ for $n\leq 10$.</p>
<p>Find the value of $n\leq 1\,000\,000$ for which $n/\phi(n)$ is a maximum.</p>

"""

import euler_math as em
from math import gcd
from time import monotonic_ns

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
    
def totatives(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: 
        phi -= phi // n 
    return phi

def solve(debug=False):
    
    res=None
    big = 0
    for n in range(2, 1_000_001):
        tn = em.totient(n)

        if n / tn > big:
            big = (n / tn)
            res = n
            
            if debug:
                print(f"{n}/{tn} ~= {big:.3f}")

                
            if debug:
                rs_start = monotonic_ns()
                rf = em.totient(n)
                rs_time = monotonic_ns() - rs_start

                py_slow_start = monotonic_ns()
                ps = phi_func(n)
                py_slow_time = monotonic_ns() - py_slow_start

                py_fast_start = monotonic_ns()
                pf = totatives(n)
                py_fast_time = monotonic_ns() - py_fast_start

                print(f"phi({n}) = {tn}")
                print('\n'.join([f"Slow Python: {ps} ns", f"Fast Python: {pf} ns", f"Rust: {tn} ns"]))
                print()
                
                assert(pf == tn)
                
    
    
    print(f"*** Answer: {res} ***")