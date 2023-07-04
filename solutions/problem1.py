"""
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
"""

def solve():
    N = 1000

    # fast
    n_3 = (N-1)//3
    n_5 = (N-1)//5
    n_15 = (N-1)//15

    tot_3 = 3*(n_3 * (n_3+1))//2
    tot_5 = 5*(n_5 * (n_5+1))//2
    tot_15 = 15*(n_15 * (n_15+1))//2
    print(f"{tot_3} + {tot_5} - {tot_15} = {tot_3+tot_5-tot_15}")

    # slow
    # total = 0
    # for i in range(1, N):
    #     if i % 3 == 0:
    #         total += i
    #     elif i % 5 == 0:
    #         total += i
        
    # print(total)