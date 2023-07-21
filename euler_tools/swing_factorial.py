
from math import isqrt
from bisect import bisect_left
from typing import Iterator
from gmpy2 import mpz, xmpz, mul


def Primes(limit: int) -> Iterator:
    '''Returns a generator that yields the prime numbers up to limit.
       https://gmpy2.readthedocs.io/en/latest/advmpz.html'''

    # Increment by 1 to account for the fact that slices  do not include
    # the last index value but we do want to include the last value for
    # calculating a list of primes.
    sieve_limit = isqrt(limit) + 1
    limit += 1

    # Mark bit positions 0 and 1 as not prime.
    bitmap = xmpz(3)

    # Process 2 separately. This allows us to use p+p for the step size
    # when sieving the remaining primes.
    bitmap[4 : limit : 2] = -1

    # Sieve the remaining primes.
    for p in bitmap.iter_clear(3, sieve_limit):
        bitmap[p * p : limit : p + p] = -1

    return bitmap.iter_clear(2, limit)


def product(s: list[int], n: int, m: int) -> mpz:
    if n > m:
        return mpz(1)
    if n == m:
        return mpz(s[n])
    k: int = (n + m) // 2
    return mul(product(s, n, k), product(s, k + 1, m))


def primeswing_factorial(n: int) -> mpz:

    small_swing: list[int] = [1, 1, 1, 3, 3, 15, 5, 35, 35, 315, 63, 693, 231,
        3003, 429, 6435, 6435, 109395, 12155, 230945, 46189, 969969, 88179,
        2028117, 676039, 16900975, 1300075, 35102025, 5014575, 145422675,
        9694845, 300540195, 300540195]

    def swing(m: int, primes: list[int]) -> mpz:
        if m < 33:
            return mpz(small_swing[m])

        s: int = bisect_left(primes, 1 + isqrt(m))
        d: int = bisect_left(primes, 1 + m // 3)
        e: int = bisect_left(primes, 1 + m // 2)
        g: int = bisect_left(primes, 1 + m)

        factors: list[int] = primes[e:g] + [x for x in primes[s:d] if (m // x) & 1 == 1]

        for prime in primes[1:s]:
            p: int = 1
            q: int = m
            while True:
                q //= prime
                if q == 0:
                    break
                if q & 1 == 1:
                    p *= prime
            if p > 1:
                factors.append(p)

        return product(factors, 0, len(factors) - 1)

    def odd_factorial(n: int, primes: list[int]) -> mpz:
        if n < 2:
            return mpz(1)
        tmp: mpz = odd_factorial(n // 2, primes)
        return mul(mul(tmp, tmp), swing(n, primes))

    def eval(n: int) -> mpz:
        if n < 0:
            raise ValueError("factorial not defined for negative numbers")

        if n == 0 or n == 1:
            return mpz(1)
        if n < 20:
            return product(list(range(2, n + 1)), 0, n - 2)

        bits: int = n - n.bit_count()

        primes: list[int] = list(Primes(n))
        return mul(odd_factorial(n, primes), 2 ** bits)

    return eval(n)
