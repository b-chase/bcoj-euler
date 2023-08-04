"""<p>The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797$, $797$, $97$, and $7$. Similarly we can work from right to left: $3797$, $379$, $37$, and $3$.</p>
<p>Find the sum of the only eleven primes that are both truncatable from left to right and right to left.</p>
<p class="smaller">NOTE: $2$, $3$, $5$, and $7$ are not considered to be truncatable primes.</p>

"""

import euler_math as em

def solve(debug=False):
    
    plist = set(em.get_primes(1_000_000))

    res=0

    for p in plist:
        if p < 10:
            continue
        sp = str(p)
        if all(int(sp[i:]) in plist for i in range(1,len(sp))) \
            and all(int(sp[:-i]) in plist for i in range(1, len(sp))):
            res += p
            if debug:
                print(p)

    print(f"*** Answer: {res} ***")