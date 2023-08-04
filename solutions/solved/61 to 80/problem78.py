# https://projecteuler.net/problem=78
"""<p>Let $p(n)$ represent the number of different ways in which $n$ coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so $p(5)=7$.</p>
<div class="margin_left">
OOOOO<br>
OOOO� �O<br>
OOO� �OO<br>
OOO� �O� �O<br>
OO� �OO� �O<br>
OO� �O� �O� �O<br>
O� �O� �O� �O� �O
</div>
<p>Find the least value of $n$ for which $p(n)$ is divisible by one million.</p>

"""

import math
import euler_math as em

saved_sums = dict()


def solve(debug=False):
    
    pc = em.PartitionsCalculator()

    res = 0

    while True:
        p = pc.partitions(res)
        if p % 1_000_000 == 0:
            break
        else:
            res += 1
            if debug and res % 1000 == 0:
                print(f"p({res}) has {int(math.log10(p))} digits")


    print(f"*** Answer: {res} ***")