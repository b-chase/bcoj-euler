# https://projecteuler.net/problem=76
"""<p>It is possible to write five as a sum in exactly six different ways:</p>
\begin{align}
&amp;4 + 1\\
&amp;3 + 2\\
&amp;3 + 1 + 1\\
&amp;2 + 2 + 1\\
&amp;2 + 1 + 1 + 1\\
&amp;1 + 1 + 1 + 1 + 1
\end{align}
<p>How many different ways can one hundred be written as a sum of at least two positive integers?</p>

"""

import euler_math as em

def solve(debug=False):
    
    saved_sums = dict()

    def ways_2_sum(num: int, max_term = None) -> int:
        if not max_term:
            max_term = num - 1
        
        if debug:
            print(f"Checking ... Ways({num}, {max_term})")
        saved = saved_sums.get((num, max_term))
        if saved:
            ways_ct = saved
        elif max_term==1:
            ways_ct = 1
        else:
            ways_ct = 0
            for n in range(1, max_term+1):
                rem = num - n
                if rem > 0:    
                    rem_max_term = min(rem, n)
                    ways_ct += ways_2_sum(rem, rem_max_term)
                else:
                    ways_ct += 1
        if debug:
            print(f"Ways({num}, {max_term}) = {ways_ct}")
        
        saved_sums[(num, max_term)] = ways_ct
        return ways_ct


    if debug: 
        for z in range(1, 15):
            print(z, ways_2_sum(z))
    
    N = 100
    res = ways_2_sum(N)
    
    print(f"*** Answer: {res} ***")