# https://projecteuler.net/problem=77
"""<p>It is possible to write ten as the sum of primes in exactly five different ways:</p>
\begin{align}
&amp;7 + 3\\
&amp;5 + 5\\
&amp;5 + 3 + 2\\
&amp;3 + 3 + 2 + 2\\
&amp;2 + 2 + 2 + 2 + 2
\end{align}
<p>What is the first value which can be written as the sum of primes in over five thousand different ways?</p>

"""

import euler_math as em

def solve(debug=False):
    
    prime_list = em.get_primes(100_000)
    
    saved_sums = dict()

    def ways_2_sum_primes(num: int, max_pi = None, level=0) -> int:
        
        level_marker = '>'*(level) + (' ' if level > 0 else '')
        
        if max_pi is None:
            max_pi = -1
            while prime_list[max_pi+1] < num:
                max_pi += 1
        if debug:
            print(level_marker + f"Checking for N={num} and max_p = {prime_list[max_pi]}")
        
        if (num, max_pi) in saved_sums:
            if debug:
                print(f"Using saved sum for {(num, max_pi)}: {saved_sums[(num, max_pi)]}")
            return saved_sums[(num, max_pi)]

        if prime_list[max_pi] == num:
            if debug:
                print(f"Number can add to itself {num}")
            ways_ct = 1  # can use itself
        else:
            ways_ct = 0

        for pi,p in enumerate(prime_list[:max_pi+1]):
            rem = num - p
            assert rem >= 0
            
            if rem <= 1:
                new_ways = 0  # can't add
            elif rem == 2:
                new_ways = 1
            # elif rem <= 4:
            #     new_ways = 1 # only one way to add to 2
            else:
                rem_max_term = 0
                for i,sp in enumerate(prime_list[:pi+1]):
                    if sp <= rem:
                        rem_max_term = i
                    else:
                        break
                if debug:
                    print(level_marker + f"[{num}-{p}]]Checking Ways(n={rem}, pi={rem_max_term})")
                new_ways = ways_2_sum_primes(rem, rem_max_term, level=level+1)
                if debug and rem == prime_list[rem_max_term]:
                    print(level_marker + f"{rem} = {prime_list[rem_max_term]} + ... ({new_ways}) [inside loop]")
            ways_ct += new_ways

            if debug:
                print(level_marker + f"{num} = {p} + ...  ({new_ways})")

        saved_sums[((num, max_pi))] = ways_ct

        return ways_ct

    assert ways_2_sum_primes(10) == 5


    k = 10

    while True:
        k += 1
        w_k = ways_2_sum_primes(k) 
        if k % 1000 == 0:
            print(k, w_k)
        if w_k > 5000:
            break

    res = k
    
    print(f"*** Answer: {res} ***")