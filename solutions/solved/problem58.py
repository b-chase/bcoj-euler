# https://projecteuler.net/problem=58
# There was a problem loading the HTML for this problem

import euler_math as em

def spiral_corners():
    # a generator that produces numbers at the corners of a 4-sided number spiral
    step = 2
    n = 1
    corners = 0
    while True:
        n += step
        yield n
        

        corners = (corners + 1) % 4
        if corners == 0:
            step += 2
        

def solve(debug=False):
    
    res = None
    numer = 0
    denom = 1

    spc = spiral_corners()
    primes = em.get_primes(1_000_000_000)
    max_prime = primes[-1]
    prime_set = set(primes)

    n = 1
    side_len = 1
    while n < max_prime:
        # check 4 numbers, add primes to numer
        for _ in range(4):
            n = spc.__next__()
            if n in prime_set:
                numer += 1
        denom += 4

        side_len += 2

        ratio = 10*numer // denom

        if debug:
            print(f"{side_len}: {numer}/{denom} = {numer / denom:.10f}")

        if ratio == 0:
            res = side_len
            break
    
    print(f"*** Answer: {res} ***")