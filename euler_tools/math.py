# euler_tools

import euler_math as em
import math

def frac_from_seq(seq: list[int]) -> tuple[int]:

    numer, denom = seq[-1], 1
    for x in seq[-2:0:-1]:
        numer, denom = x*numer + denom, numer
        gdiv = math.gcd(numer, denom)
        numer //= gdiv
        denom //= gdiv
    
    numer, denom = denom, numer
    numer += seq[0]*denom

    return (numer, denom)

def get_digits(n:int) -> list[int]:
    d = [n%10]
    m = n//10
    while m:
        d.append(m%10)
        m//=10
    d.reverse()
    return d


def digits_to_num(digits):
    return int(''.join(str(x) for x in digits))


def is_pent(pn) -> bool:
        gn = em.int_sqrt((2 * pn) // 3)
        
        for i in range(2):
            guess_n = gn+i
            tmp = guess_n*(3*guess_n-1)

            if tmp // 2 == pn:
                return True
        return False


def permute_down(pattern: list) -> bool:
    """Permutes the pattern in place, from high to low.

    Args:
        pattern (list): a list of items that can be compared ordinally

    Returns:
        bool: True if permutation is possible, False if it is not
    """
    if len(pattern) == 1:
        return False
    else:
        changed = False
        # new_pattern = pattern.copy()
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
                pattern[j:] = tail
                changed = True
                break
        
        return changed