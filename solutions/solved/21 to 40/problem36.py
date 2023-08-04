"""<p>The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.</p>
<p>Find the sum of all numbers, less than one million, which are palindromic in base $10$ and base $2$.</p>
<p class="smaller">(Please note that the palindromic number, in either base, may not include leading zeros.)</p>

"""

"""
Palindrome numbers in base2:
1
11
101
111
1001
1111
10001
10101
11011
11111
"""

import euler_math as em

def solve(debug=False):
    
    def is_pali10(num) -> bool:
        snum = str(num)
        return snum == snum[::-1]

    def is_pali2(num) -> bool:
        snum = bin(num)[2:]
        return snum == snum[::-1]

    res = 0
    for n in range(1, 1_000_000,2):
        if is_pali10(n) and is_pali2(n):
            res += n
            if debug:
                print(n, bin(n)[2:])
    
    print(res)