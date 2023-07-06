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

import euler_math as em

def solve(debug=False):
    rec_min = 3

    best, res = 0, 0
    for n in range(1,1000):
        if n < 11:
            m = 10
        elif n < 101:
            m = 100
        elif n < 1001:
            m = 1000
        
        rec = 0
        digits = []
        while True:
            d = m // n
            rem = m % n
            digits.append(d)
            if rem == 0:
                break
            else:
                m = rem * 10

            print(n, digits)
            for i in range(len(digits)//3):
                pattern = digits[0:i]
                if pattern == digits[(i+1):(2*i)] and pattern == digits[(2*i+1):(3*i)]:
                    rec = 3
                    digits = pattern
                    break
            if rec > 0:
                if len(digits) > best:
                    best, res = len(digits), n
                    break
        print(res)
                



