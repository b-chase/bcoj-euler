
from math import prod, factorial as pyfact
import euler_math as em

small_factorials = [pyfact(i) for i in range(0,21)]


def basic_fact(n):
    return prod(i for i in range(1,n+1))


def twobit_fact(n):

    bits = 0
    res = 1
    for z in range(1,n+1):
        while not z & 1:
            z = z >> 1
            bits += 1
        res *= z
    
    return res << bits


def even_odd_fact(n):
    if n <  len(small_factorials):
        return small_factorials[n]
    
    res = 1
    if n & 1:
        res *= n
        n -= 1
    
    half_n = n//2

    res *= even_odd_fact(half_n)
    for i in range(1,n+1,2):
        res *= i
    
    return res << half_n


def prime_fact(n):
    if n < 2: # len(small_factorials):
        return small_factorials[n]
    
    primes_to_n = em.get_primes(n)

    res = 1

    for p in primes_to_n:
        pow = n // p
        res *= p**pow

    return res #<< (n//2)


# for z in range(30):
#     print(z, pyfact(z))

#     assert basic_fact(z) == pyfact(z)
#     assert twobit_fact(z) == pyfact(z)
#     assert even_odd_fact(z) == pyfact(z)
#     try:
#         assert prime_fact(z) == pyfact(z)
#     except Exception as e:
#         print(f"Error computing {z}!: {prime_fact(z)}, expected {pyfact(z)}")
#         raise(e)
