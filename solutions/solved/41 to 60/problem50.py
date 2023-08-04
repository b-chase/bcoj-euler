"""<p>The prime $41$, can be written as the sum of six consecutive primes:</p>
$$41 = 2 + 3 + 5 + 7 + 11 + 13.$$
<p>This is the longest sum of consecutive primes that adds to a prime below one-hundred.</p>
<p>The longest sum of consecutive primes below one-thousand that adds to a prime, contains $21$ terms, and is equal to $953$.</p>
<p>Which prime, below one-million, can be written as the sum of the most consecutive primes?</p>
"""

import euler_math as em

def solve(debug=False):
    
    plist = em.get_primes(1000_000)
    pset = set(plist)
    
    res=0

    top = 0

    for i in range(len(plist)-1):
        for j in range(i+1, len(plist)):
            p = sum(plist[i:j])
            if p > 1_000_000:
                break
            if p in pset and (j-i) > top:
                res = p
                top = j-i
        if debug:
            print(f"Starting from {plist[i]}: top was P={res} ({top} terms)")
    
    print(f"*** Answer: {res} ***")



