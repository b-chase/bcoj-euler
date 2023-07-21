"""<p>If we take $47$, reverse and add, $47 + 74 = 121$, which is palindromic.</p>
<p>Not all numbers produce palindromes so quickly. For example,</p>
\begin{align}
349 + 943 &amp;= 1292\\
1292 + 2921 &amp;= 4213\\
4213 + 3124 &amp;= 7337
\end{align}
<p>That is, $349$ took three iterations to arrive at a palindrome.</p>
<p>Although no one has proved it yet, it is thought that some numbers, like $196$, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, $10677$ is the first number to be shown to require over fifty iterations before producing a palindrome: $4668731596684224866951378664$ ($53$ iterations, $28$-digits).</p>
<p>Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is $4994$.</p>
<p>How many Lychrel numbers are there below ten-thousand?</p>
<p class="smaller">NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.</p>
"""

import euler_math as em
from euler_tools.math import get_digits, digits_to_num

def reverse_number(num) -> int:
    return digits_to_num(get_digits(num)[::-1])

def solve(debug=False):
    res=None
    
    lychrels = set()
    checked = set()
    
    for n in range(1, 10000):
        if n in checked:
            continue
        r = reverse_number(n)
        if r < n:
            chain = [n]
        else:
            chain = [n, r]
        
        # generate next numbers
        t = r + n
        r = reverse_number(t)
        counter = 0
        limit, limit_set = float('Inf'), False
        while counter < limit:
            counter += 1
            if t == r:
                for x in chain:
                    checked.add(x)
                chain = []
                break
            else:
                if r < t:
                    chain.append(t)
                else:
                    chain.extend([t,r])
                t = t + r
                r = reverse_number(t)
            
            if t > 10000 and not limit_set:
                limit, limit_set = counter+51, True
            
        # empty chain into lychrels if it's not set
        for z in chain:
            if z == 97:
                print(chain)
            if z < 10000:
                checked.add(z)
                lychrels.add(z)       
            
    
    if debug:
        for z in sorted(list(lychrels)):
            print(z)
            
    print(f"*** Answer: {len(lychrels)} ***")