"""<p>It is possible to show that the square root of two can be expressed as an infinite continued fraction.</p>
<p class="center">$\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$</p>
<p>By expanding this for the first four iterations, we get:</p>
<p>$1 + \frac 1 2 = \frac  32 = 1.5$<br>
$1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$<br>
$1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$<br>
$1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$<br></p>
<p>The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.</p>
<p>In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?</p>

"""

import euler_math as em
from math import log10

def solve(debug=False):
    # sqrt(2) fractional approximations come from Pell Numbers: 0, 1, 2, 5, 12, 29,  ...
    # P_n = (2(P_n-1) + P_n-2)
    # sqrt(2) ~ ( P_n + P_n-1 ) / P_n-1

    res=0

    pells = em.pell_numbers(1010)  # zero-indexed

    if debug:
        print(pells[:10])
    for i in range(1000):
        denom = pells[i+2]
        numer = pells[i+2] + pells[i+1]

        if len(str(numer)) > len(str(denom)):
            res += 1
            if debug:
                print(f"{i}: ({int(log10(numer))}:{int(log10(denom))}) sqrt(2) ~= {numer/denom:.6f}")

    
    print(f"*** Answer: {res} ***")