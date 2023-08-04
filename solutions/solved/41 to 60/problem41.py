"""<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.</p>
<p>What is the largest $n$-digit pandigital prime that exists?</p>

"""

import euler_math as em

def solve(debug=False):

    # plist = em.get_primes(987654321)
    # primes = set(plist)
    # if debug:
    #     print("primes loaded")

    def is_pandigit(n:int) -> bool:
        sn = str(n)
        digits = set(sn)
        if len(digits) < len(sn):
            return False
        
        expected_digits = set(str(d) for d in range(1, len(sn)+1))
        return digits == expected_digits
    
    def is_prime(n): 
        return len(em.divisors_of_n(n)) == 2
    
    def permute_down(pattern: list) -> list:
        if len(pattern) == 1:
            return None
        else:
            fixed = False
            new_pattern = pattern.copy()
            for d in range(1, len(pattern)):
                i = - (d)
                j = - (d + 1)

                if pattern[i] < pattern[j]:
                    # pattern[j] is higher than next digit, so switch 
                    tail = pattern[j:]
                    repl = max(x for x in tail if x < pattern[j])
                    tail.remove(repl)
                    tail.sort(reverse=True)
                    tail.insert(0, repl)
                    new_pattern[j:] = tail
                    fixed = True
                    break
            if not fixed:
                return None
            return new_pattern
    
    x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    res = 0

    while x and res == 0:
        while sum(x) % 3 == 0:
            x.pop(0)

        z = x.copy()
        if debug:
            print(f"Permutations of length {len(z)} starting with {z}")

        while z:
            n = int(''.join(str(d) for d in z))
            if debug:
                if not is_pandigit(n):
                    print("Error, not pandigital:", n)
                    raise AssertionError
            
            if is_prime(n):
                res = n
                break
            else:
                if debug:
                    y = z.copy()
                z = permute_down(z)

                if debug and not z:
                    print(y, n)
                
        
        # if we reach the end, permute again with less digits of X:
        assert x[0] == max(x)
        x.pop(0)

    print(f"*** Answer: {res} ***")