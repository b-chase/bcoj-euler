"""<p>A unit fraction contains $1$ in the numerator. The decimal representation of the unit fractions with denominators $2$ to $10$ are given:</p>
\begin{align}
1/2 &amp;= 0.5\\
1/3 &amp;=0.(3)\\
1/4 &amp;=0.25\\
1/5 &amp;= 0.2\\
1/6 &amp;= 0.1(6)\\
1/7 &amp;= 0.(142857)\\
1/8 &amp;= 0.125\\
1/9 &amp;= 0.(1)\\
1/10 &amp;= 0.1
\end{align}
<p>Where $0.1(6)$ means $0.166666\cdots$, and has a $1$-digit recurring cycle. It can be seen that $1/7$ has a $6$-digit recurring cycle.</p>
<p>Find the value of $d \lt 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.</p>

"""
from dataclasses import dataclass
import euler_math as em


@dataclass
class Answer:
    num:int 
    size:int
    

def solve(debug=False):
    
    N = 1000
    max_digits = 2000
    
    res = Answer(0, 0)
    
    for d in range(1,N):
        digits = []
        m = 10
        
        while len(digits) < max_digits:
            if m < d:
                m *= 10
                digits.append(0)
                continue
            else:
                digits.append(m // d)
                rem = m % d
                m = rem*10
        
        period = em.periodicity(digits)
        if period.period_length and period.period_length > res.size:
            res = Answer(d, period.period_length)
            
            if debug:
                print(res)
                print(period.pattern)
                print(1/d)
        
    print(f"*** Answer: {res} ***")
                
        
        

