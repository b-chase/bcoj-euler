"""<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
"""

import euler_math as em

def solve(debug=False):
    N = 100
    
    naturals_sum = em.sum_to_n(N)
    
    sq_nat_sum = sum(x**2 for x in range(1,101))
    
    print(naturals_sum**2 - sq_nat_sum)
    # +1 +3 +5 +7 ...
    