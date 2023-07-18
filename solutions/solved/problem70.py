# https://projecteuler.net/problem=70
"""<p>Euler's totient function, $\phi(n)$ [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $\phi(9)=6$.<br>The number $1$ is considered to be relatively prime to every positive number, so $\phi(1)=1$. </p>
<p>Interestingly, $\phi(87109)=79180$, and it can be seen that $87109$ is a permutation of $79180$.</p>
<p>Find the value of $n$, $1 \lt n \lt 10^7$, for which $\phi(n)$ is a permutation of $n$ and the ratio $n/\phi(n)$ produces a minimum.</p>

"""

import euler_math as em

def solve(debug=False):

    plist = em.get_primes(100_000)
    res=None
    low = float('inf')

    # for n in range(1_000_000, 10_000_000):
    prime_products = []
    for i, p_i in enumerate(plist[:-1]):
        for p_j in plist[i+1:]:
            n = p_i * p_j
            if n > 1e7:
                break
            tn = (p_i - 1) * (p_j - 1)
            prime_products.append((n, tn))
    
    for n, tn in prime_products:
        
        # phi_n = em.totient(n)
        # assert tn == phi_n
        phi_n = tn
        
        ratio = n / phi_n
        if ratio < low:
            if tuple(sorted(str(n))) == tuple(sorted(str(phi_n))):
                if debug:
                    print(f"phi({n}) = {phi_n}")

                low, res = ratio, n


    print(f"*** Answer: {res} ***")