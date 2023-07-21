"""<p>A googol ($10^{100}$) is a massive number: one followed by one-hundred zeros; $100^{100}$ is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only $1$.</p>
<p>Considering natural numbers of the form, $a^b$, where $a, b \lt 100$, what is the maximum digital sum?</p>

"""

import euler_math as em
from euler_tools.math import get_digits
def solve(debug=False):
    
    res=0
    
    for a in range(91,100):
        for b in range(91,100):
            a_b = a**b
            digits = get_digits(a_b)
            digit_sum = sum(digits)
            res = max(digit_sum, res)
            
            if debug:
                print(f"Sum digits[{a}^{b}] = {digit_sum}")
    
    print(f"*** Answer: {res} ***")