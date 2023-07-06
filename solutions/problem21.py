"""<p>Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
<p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
<p>Evaluate the sum of all the amicable numbers under $10000$.</p>
"""

import euler_math as em

def solve(debug=False):
    
    sum_div_list = []
    
    N = 10_000
    
    amicable_pair_sums = []
    
    for x in range(0,N):
        div_list = em.divisors_of_n(x)[:-1]
        d_n = sum(div_list)
        sum_div_list.append(d_n)
        
        if d_n < x and sum_div_list[d_n]==x:
            amicable_pair_sums.append(x+d_n)
            if debug:
                print(f"Amicable pair: {d_n} and {x}")
    
    print(sum(amicable_pair_sums))
        
    