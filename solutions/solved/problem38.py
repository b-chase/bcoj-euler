"""<p>Take the number $192$ and multiply it by each of $1$, $2$, and $3$:</p>
\begin{align}
192 \times 1 &amp;= 192\\
192 \times 2 &amp;= 384\\
192 \times 3 &amp;= 576
\end{align}
<p>By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$.</p>
<p>The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.</p>
<p>What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1,2, \dots, n)$ where $n \gt 1$?</p>

"""

import euler_math as em

def solve(debug=False):
    
    def pandigit_test(n:int|str) -> bool:
        sn = set(str(n))
        return '0' not in sn and len(sn)==9

    res=0

    
    def pandigitals():
        limit = 987654321
        while limit > 1e8:
            yield limit
            limit -= 1
            while not pandigit_test(limit):
                limit -=1
        return None

    for n in range(9999, 0, -1):
        while True:
            t = 2
            z = ''.join(str(n*i) for i in range(1,t+1))
            if pandigit_test(z):
                print(t, n)
                res = int(z)
                break

            if len(z) >= 9:
                break
        
        if res > 0:
            break
            
    

    print(f"*** Answer: {res} ***")