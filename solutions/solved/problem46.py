"""<p>It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.</p>
\begin{align}
9 = 7 + 2 \times 1^2\\
15 = 7 + 2 \times 2^2\\
21 = 3 + 2 \times 3^2\\
25 = 7 + 2 \times 3^2\\
27 = 19 + 2 \times 2^2\\
33 = 31 + 2 \times 1^2
\end{align}
<p>It turns out that the conjecture was false.</p>
<p>What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?</p>

"""

import euler_math as em

def solve(debug=False):
    
    res=None
    
    def is_prime(n:int) -> bool:
        return len(em.divisors_of_n(n))==2


    primes = set()
    squares = set()

    def confirms_goldbach(n: int) -> bool:
        if is_prime(n):
            primes.add(n)
            return True
        elif n%2==0:
            return True
        for p in primes:
            if p > n:
                break
            tmp = n - p
            if (tmp // 2) in squares:
                return True
        return False
    
    x = 1

    while confirms_goldbach(x) or x==1:
        squares.add(x**2)
        x += 1

    res = x

    if debug:
        print(res, confirms_goldbach(res))
        print(primes)
        print(squares)


    print(f"*** Answer: {res} ***")