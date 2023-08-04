"""<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.</p>

<p>The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.</p>

<p>Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.</p>

<div class="note">HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div>

"""

import euler_math as em

def solve(debug=False):
    pandigitals = []
    
    for a in range(2,200):
        sa = str(a)
        set_a = set(sa)
        if '0' in sa or len(set_a) < len(sa):
            continue
            
        for b in range(a+1, 5000):
            sb = str(b)
            set_b = set(sb)
            if '0' in sb or len(set_b) < len(sb) \
              or len(set_a.intersection(set_b)) > 0:
                continue
            
            x = a * b
            sx = str(x)
            if len(sx) + len(sa) + len(sb) > 9:
                # means b has gotten too large
                break
            
            set_x = set(sx)
            if '0' in sx or len(set_x.intersection(set_a))>0 \
              or len(set_x.intersection(set_b))>0 \
              or len(sx) > len(set_x):
                continue
            
            if len(set_x) + len(set_a) + len(set_b) == 9:
                pandigitals.append((a, b, x))
                if debug:
                    print(f"{a} x {b} = {x}")
            
    res = sum(set([p[2] for p in pandigitals]))
            
    print(res)
    