# https://projecteuler.net/problem=63
"""<p>The $5$-digit number, $16807=7^5$, is also a fifth power. Similarly, the $9$-digit number, $134217728=8^9$, is a ninth power.</p>
<p>How many $n$-digit positive integers exist which are also an $n$th power?</p>

"""

import euler_math as em

def solve(debug=False):
    
    res=0

    for base in range(1,10):
        num = base
        power = 1
        
        while len(str(num)) == power:
            if debug:
                print(f"{base}^{power} = {num}")
                
            res += 1
            num *= base
            power += 1

            
    
    print(f"*** Answer: {res} ***")