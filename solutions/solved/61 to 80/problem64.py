# https://projecteuler.net/problem=64
"""<p>All square roots are periodic when written as continued fractions and can be written in the form:</p>

<p>It can be seen that the sequence is repeating. For conciseness, we use the notation $\sqrt{23}=[4;(1,3,1,8)]$, to indicate that the block (1,3,1,8) repeats indefinitely.</p>

<p>Exactly four continued fractions, for $N \le 13$, have an odd period.</p>
<p>How many continued fractions for $N \le 10\,000$ have an odd period?</p>

"""

import euler_math as em

def solve(debug=False):
    
    res = 0
    lng = 0
    for x in range(1, 10_001):
        x_frac = em.root_cont_fraction(x, 1000)
        p = em.periodicity(x_frac)

        if p.period_length and p.period_length % 2 == 1:
            res += 1

            if debug:
                print(x, p.period_length)
                lng = max(lng, p.period_length)


        # print(f"sqrt({x}) =", em.int_sqrt(x), x_frac)

    if debug:
        print("Longest was: ", lng)
    
    print(f"*** Answer: {res} ***")