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
from solutions.euler_tools import frac_from_seq

def solve(debug=False):
    res=(0,0)

    unsolved = []

    for D in range(2,1001):
        if debug:
            print(f"\n{D}: ", end="")
        if em.int_sqrt(D)**2 == D:
            continue
        unsolved.append(D)
        y = 1
        while y < 1000:
            x2 = 1 + D*(y**2)
            x = em.int_sqrt(x2)

            if x**2 == x2:
                unsolved.pop()
                if debug:
                    print(f" {x}^2 - {D}*{y}^2 = 1", end="")
                if x > res[1]:
                    res = (D, x)
                break

            y += 1
        
    # print(unsolved)
    print("\nNow for still unsolved: ")
    for ud in unsolved:
        if debug:
            print(f"\n{ud}: ", end="")
        u_frac = em.RootContFraction(ud)
        while True:
            u_frac.next()
            convergent = frac_from_seq(u_frac.terms)
            try_x = convergent[0]
            try_y = convergent[1]
            if try_x**2 - ud*try_y**2 == 1:
                if debug:
                    print(f" {try_x}^2 - {ud}*{try_y}^2 = 1", end="")
                if try_x > res[1]:
                    res = (ud, try_x)
                break

    print(f"\n\n*** Answer: {res} ***")