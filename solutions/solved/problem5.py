"""<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <dfn class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></dfn> by all of the numbers from $1$ to $20$?</p>

"""

import euler_math as em

def solve(debug=False):
    primes = em.get_primes(20)
    
    res = 1
    
    for p in primes:
        res *= p
    
    # 4, 8, 16
    # 9
    
    res *= 2*2*2 * 3
    print(res)
	