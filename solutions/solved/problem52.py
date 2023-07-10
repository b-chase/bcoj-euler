"""<p>It can be seen that the number, $125874$, and its double, $251748$, contain exactly the same digits, but in a different order.</p>
<p>Find the smallest positive integer, $x$, such that $2x$, $3x$, $4x$, $5x$, and $6x$, contain the same digits.</p>

"""

import euler_math as em
from solutions.euler_tools import digits_to_num, get_digits

def solve(debug=False):
    
    res=None

    digits = [1, 1]
    x = 11

    for _ in range(100_000):
        if digits[1] > 6:
            digits = [1] + [0]*(len(digits)-1) + [1]
        
        digit_set = set(digits)

        x = digits_to_num(digits)

        if all(set(get_digits(t*x))==digit_set for t in range(2, 6+1)):
            res = x
            if debug:
                print([t*x for t in range(1, 6+1)])
            break

        x += 1
        digits = get_digits(x)


    
    print(f"*** Answer: {res} ***")