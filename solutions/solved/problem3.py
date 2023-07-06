"""<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>
"""

import euler_math as em

def solve():
	n = 600851475143
	primes = em.get_primes(em.int_sqrt(n))

	for p in primes:
		if n % p == 0:
			n //= p
		
		if n == 1:
			print(p)
			break