"""<p>Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
\begin{align}
1634 &amp;= 1^4 + 6^4 + 3^4 + 4^4\\
8208 &amp;= 8^4 + 2^4 + 0^4 + 8^4\\
9474 &amp;= 9^4 + 4^4 + 7^4 + 4^4
\end{align}
</p><p class="smaller">As $1 = 1^4$ is not a sum it is not included.</p>
<p>The sum of these numbers is $1634 + 8208 + 9474 = 19316$.</p>
<p>Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.</p>

"""

import euler_math as em

def digits_of_n(n:int) -> list[int]:
    return [int(x) for x in str(n)]
    

def solve(debug=False):
    
    search_range = range(2, 6*(9**5))
    
    found = []
    
    for x in search_range:
        digits_x = digits_of_n(x)
        tmp = 0
        for d in digits_x:
            tmp += d**5
            if tmp > x:
                break
        if tmp == x:
            found.append(x)
    
    print(found)
    print(sum(found))