"""<p>The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.</p>
<p>Let $d_1$ be the $1$<sup>st</sup> digit, $d_2$ be the $2$<sup>nd</sup> digit, and so on. In this way, we note the following:</p>
<ul><li>$d_2d_3d_4=406$ is divisible by $2$</li>
<li>$d_3d_4d_5=063$ is divisible by $3$</li>
<li>$d_4d_5d_6=635$ is divisible by $5$</li>
<li>$d_5d_6d_7=357$ is divisible by $7$</li>
<li>$d_6d_7d_8=572$ is divisible by $11$</li>
<li>$d_7d_8d_9=728$ is divisible by $13$</li>
<li>$d_8d_9d_{10}=289$ is divisible by $17$</li>
</ul><p>Find the sum of all $0$ to $9$ pandigital numbers with this property.</p>

"""

import euler_math as em
from solutions.euler_tools import permute_down

def solve(debug=False):
    
    res=0
    
    num = list(int(x) for x in '9876543210')
    plist = enumerate([2, 3, 5, 7, 11, 13, 17])
    
    while num[0] > 0:
        
        for i, p in plist:
            sub_digits = num[i+1:i+4]
            num = sub_digits[0]*100 + sub_digits[1]*10 + sub_digits[2]
            
        break
        
    
    print(f"*** Answer: {res} ***")