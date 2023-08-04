"""<p>The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.</p>
<p>There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.</p>
<p>How many circular primes are there below one million?</p>

"""

import euler_math as em

def solve(debug=False):

    N = 1000_000
    
    plist = set(em.get_primes(N))

    evens = set(['0', '2', '4', '6', '8'])

    ok_primes = set()
    bad_primes = set()

    for p in plist:
        if p < 10:
            ok_primes.add(p)
            continue

        digits = set(str(p))
        
        if not evens.isdisjoint(digits):
            bad_primes.add(p)
        
        else:
            if debug:
                print(p)
            m = int(str(p)[1:])*10 + int(str(p)[0])

            while m != p:
                if debug:
                    print(m, p)

                if m not in plist:
                    break

                m = int(str(m)[1:])*10 + int(str(m)[0])
            
            if m == p:
                ok_primes.add(p)
    
    print(len(ok_primes))
                
                


    pass