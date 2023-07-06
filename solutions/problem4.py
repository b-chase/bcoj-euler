"""<p>A palindromic number reads the same both ways. 
The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

"""

import euler_math as em

def is_palindromic(n:int) -> bool:
    
    digits = []
    rem = n-0
    while rem > 0:
        digits.append(rem % 10)
        rem //= 10
        
    while len(digits)>1:
        if digits.pop(-1) != digits.pop(0):
            return False
    return True

def solve(debug=False):
    t = 1e6
    while t > 1e5:
        t -= 1
        if not is_palindromic(t):
            continue
        
        max_d = 999
        if debug:
            print(f"t={t}, max_d={max_d}")
        for d1 in range(100,max_d):
            if t % d1 == 0:
                d2 = t // d1
                if d2 >= 1e3:
                    continue
                elif d2 < 100:
                    max_d = d1
                    break
                else:
                    print(t)
                    return
                
                
                
    

