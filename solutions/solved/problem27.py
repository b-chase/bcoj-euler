"""<p>Euler discovered the remarkable quadratic formula:</p>
<p class="center">$n^2 + n + 41$</p>
<p>It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.</p>
<p>The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.</p>
<p>Considering quadratics of the form:</p>
<blockquote>
$n^2 + an + b$, where $|a| &lt; 1000$ and $|b| \le 1000$<br><br><div>where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$</div>
</blockquote>
<p>Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.</p>
"""

import euler_math as em
from dataclasses import dataclass

@dataclass
class Answer:
    a: int
    b: int
    value: int

class NotPrimeError(ValueError):
    pass

def solve(debug=False):
    pl = set(em.get_primes(10_000))
    if debug:
        print("Primes loaded")
        
    sq_n = [n**2 for n in range(0,2000)]
    
    best = Answer(None, None, 0)
    for a in range(-999, 1000):
        an = [a*n for n in range(0, 2000)]
        for b in range(-1000, 1001):
            n = 0
            test_p = sq_n[n] + an[n] + b
            while test_p in pl:
                n += 1
                test_p = sq_n[n] + an[n] + b
                
            
            if n > best.value:
                best = Answer(a, b, n)
                if debug:
                    print("** New Best **")
            
                if debug:
                    print(Answer(a, b, n))
                
        
    print(f"*** Answer: {best} ***")
    print(best.a * best.b)
    pass