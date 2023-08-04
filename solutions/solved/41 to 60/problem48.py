"""<p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
<p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>

"""

import euler_math as em

def solve(debug=False):
    
    res=0

    ending = lambda x: x % int(1e10)

    for x in range(1, 1001):
        res = ending(res + x**x)
    
    print(f"*** Answer: {res} ***")