# euler_tools

import euler_math as em
import math
from collections import Counter

roman_numerals = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

inv_roman_numerals = [(v,k) for k,v in roman_numerals.items()]
inv_roman_numerals.sort(key=lambda x: x[0], reverse=True)

def roman_numeral_to_int(rn:str) -> int:
    res = 0
    numerals = [roman_numerals[c] for c in rn]
    
    i = 0
    # iterate through number, adding up values
    while i < len(numerals)-1:
        num = numerals[i]
        next_num = numerals[i+1]
        # if it's a subtraction, modify and increment index
        if next_num > num:
            num = next_num - num
            i += 1
        # sum to total
        res += num
        i += 1
    # if we didn't skip the ending with a subtraction pair, increment by that value too
    if i == len(numerals)-1:
        res += numerals[-1]
    return res

def int_to_roman_numeral(x:int) -> str:
    res = ''
    i = 0
    rem = x
    while i < len(inv_roman_numerals):
        rn_val, rn_char = inv_roman_numerals[i]
        char_ct = rem // rn_val
        # update string and remainder
        res += char_ct * rn_char
        rem %= rn_val
        # check if we should use a subtraction
        # or just do a replace later  <- this is the way
        i += 1
    
    replacements = [
        ('VIIII', 'IX'), ('IIII', 'IV'), 
        ('LXXXX', 'XC'), ('XXXX', 'XL'),
        ('DCCCC', 'CM'), ('CCCC', 'CD')
    ]
    
    for bad, good in replacements:
        res = res.replace(bad, good)
    
    return res
        

def generate_pythagorean_triples(M):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    triples = set()
    m = 2
    while True:
        for n in range(1, m):
            # if (m - n) % 2 == 1 and gcd(m, n) == 1:
            if True:
                # Generate Pythagorean triple
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                
                a,b = min(a,b), max(a,b)
                if a > M:
                    if n == 1:
                        return triples
                    else:
                        break
                
                d=1
                while d*a <= M:            
                    triples.add((d*a, d*b, d*c))
                    d += 1
        m += 1



def roll_dice_combos(max_roll, dice_count, debug=False) -> Counter:
    # returns a counter with the number of ways for each tuple combination
    combo_list = Counter()
    if dice_count == 1:
        combo_list = Counter(list((x,) for x in range(1, max_roll+1)))
    else:
        for x in range(1, max_roll+1):            
            # get list of possible combos for remaining dice, with values up to and including rolled value
            sub_combo_list = roll_dice_combos(x, dice_count-1, debug)
            for combo, count in sub_combo_list.items():
                # for each sub-combo, prepend the rolled value and add count to overall total
                # mult = count - sum(1 for y in combo if y == x)
                combo_list[(x,)+combo] += dice_count*count // (1+sum(1 for y in combo if y == x))
            
            # degenerate case will always have value of '1'
            combo_list[tuple([x]*dice_count)] = 1

    if debug:
        print(max_roll, dice_count, combo_list)
    return combo_list



# formerly "ways_2_sum"
def partitions(num: int, max_term = None, saved_sums = {}) -> int:
        if not max_term:
            max_term = num - 1
        
        saved = saved_sums.get((num, max_term))
        if saved:
            ways_ct = saved
        elif max_term==1:
            ways_ct = 1
        else:
            ways_ct = 0
            for n in range(1, max_term+1):
                rem = num - n
                if rem > 0:    
                    rem_max_term = min(rem, n)
                    new_ways = partitions(rem, rem_max_term, saved_sums)
                    saved_sums[(rem, rem_max_term)] = new_ways
                    ways_ct += new_ways
                    
                else:
                    ways_ct += 1
        
        saved_sums[(num, max_term)] = ways_ct
        return ways_ct


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