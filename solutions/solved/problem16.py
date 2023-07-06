"""<p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
<p>What is the sum of the digits of the number $2^{1000}$?</p>

"""

import euler_math as em

def solve(debug=False):
    s = str(2**1000)
    res = sum(int(x) for x in s)
    
    print(res)
    