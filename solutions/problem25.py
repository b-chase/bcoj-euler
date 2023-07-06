"""<p>The Fibonacci sequence is defined by the recurrence relation:</p>
<blockquote>$F_n = F_{n - 1} + F_{n - 2}$, where $F_1 = 1$ and $F_2 = 1$.</blockquote>
<p>Hence the first $12$ terms will be:</p>
\begin{align}
F_1 &amp;= 1\\
F_2 &amp;= 1\\
F_3 &amp;= 2\\
F_4 &amp;= 3\\
F_5 &amp;= 5\\
F_6 &amp;= 8\\
F_7 &amp;= 13\\
F_8 &amp;= 21\\
F_9 &amp;= 34\\
F_{10} &amp;= 55\\
F_{11} &amp;= 89\\
F_{12} &amp;= 144
\end{align}
<p>The $12$th term, $F_{12}$, is the first term to contain three digits.</p>
<p>What is the index of the first term in the Fibonacci sequence to contain $1000$ digits?</p>

"""

import euler_math as em
from math import log10

def solve(debug=False):
    f = em.Fibonacci()

    for _ in range(50):
        f.incr()
    phi = f.num / f.prev
    f_0 = f.num / (phi**51)
    
    # print(phi)
    # print(f_0)

    # F_n ~ 55 * phi**(n-10)   for n > 10
    def fib(n):
        return f_0 * phi**n

    # log10(fib_m) >= 999
    # log10(f_0 * phi**m) >= 999
    # log10(f_0) + m*log10(phi) >= 999
    # m >= (999 - log10(f_0)) / log10(phi)
    
    m = (999 - log10(f_0)) / log10(phi)
    print(m)