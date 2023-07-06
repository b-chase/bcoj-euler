"""<p>$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.</p>
<p>Find the sum of all numbers which are equal to the sum of the factorial of their digits.</p>
<p class="smaller">Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.</p>

"""

import euler_math as em

def digits_of_n(n):
    return [int(x) for x in str(n)]

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)

factorials = [factorial(a) for a in range(0,10)]

def solve(debug=False):
    # limit digits to N where 9! < 1eN
    # limit N => N*9! < 1eN
    N = 1
    while N*factorial(9) >= 10**N:
        N += 1
    
    if debug:
        print("limit =", N)
        
    tot = 0
    
    n = 3
    
    while n < 10**N:
        digits = digits_of_n(n)
        tmp = 0
        for d in digits:
            tmp += factorials[d]
            if tmp > n:
                break
        if tmp == n:
            tot += tmp
            if debug:
                digit_plus = ' + '.join([str(z)+'!' for z in digits])
                print(f"{tmp} = {digit_plus}")
        n += 1
        
    print(f"*** Answer: {tot} ***")
        
        