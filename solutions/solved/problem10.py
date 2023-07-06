"""<p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
<p>Find the sum of all the primes below two million.</p>



"""

import euler_math as em

def solve(debug=False):
    plist = em.get_primes(int(2e6))
    print(sum(plist))
	