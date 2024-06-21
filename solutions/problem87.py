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

def solve(debug=False):
    
    res=None
    
    print(f'*** Answer: {res} ***')