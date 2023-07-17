# https://projecteuler.net/problem=66
"""<p>Consider quadratic Diophantine equations of the form:
$$x^2 - Dy^2 = 1$$</p>
<p>For example, when $D=13$, the minimal solution in $x$ is $649^2 - 13 \times 180^2 = 1$.</p>
<p>It can be assumed that there are no solutions in positive integers when $D$ is square.</p>
<p>By finding minimal solutions in $x$ for $D = \{2, 3, 5, 6, 7\}$, we obtain the following:</p>
\begin{align}
3^2 - 2 \times 2^2 &amp;= 1\\
2^2 - 3 \times 1^2 &amp;= 1\\
{\color{red}{\mathbf 9}}^2 - 5 \times 4^2 &amp;= 1\\
5^2 - 6 \times 2^2 &amp;= 1\\
8^2 - 7 \times 3^2 &amp;= 1
\end{align}
<p>Hence, by considering minimal solutions in $x$ for $D \le 7$, the largest $x$ is obtained when $D=5$.</p>
<p>Find the value of $D \le 1000$ in minimal solutions of $x$ for which the largest value of $x$ is obtained.</p>

"""

import euler_math as em

def solve(debug=False):
    res=(0,0)

    big_club = []

    for D in range(2,1001):
        if em.int_sqrt(D)**2 == D:
            continue
        
        a, b = 1, 1
        smallest_res = float('Inf')
        while True:
            y = a * b
            tmp_2x = a * (D + b**2)
            if tmp_2x % 2 == 1:
                b += 1
            
            x = em.int_sqrt(x2)
            if x**2 == x2:
                if debug:
                    print(f"{D}: {x}^2 - {D}*{y}^2 = 1")
                if x > res[1]:
                    res = (D, x)
                break

    print("Large x,y for D = ", big_club)
    print(len(big_club))
    print(f"*** Answer: {res} ***")