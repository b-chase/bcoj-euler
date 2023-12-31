"""<p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.</p>
<p>A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.</p>

<p>As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p>
<p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p>

"""

import euler_math as em

def solve(debug=False):
    N = 28123
    
    abundant_nums = []
    
    for x in range(N):
        sum_div_x = sum(em.divisors_of_n(x)[:-1])
        if sum_div_x > x:
            abundant_nums.append(x)
    
    abundant_ct = len(abundant_nums)

    not_abundant_sum = [1] * N

    for i in range(1, abundant_ct):
        a = abundant_nums[i]
        for j in range(i, abundant_ct):
            b = abundant_nums[j]
            if a+b >= N:
                break
            not_abundant_sum[a+b] = 0

    res = sum(i for i, x in enumerate(not_abundant_sum) if x==1)
    print(res)
    
    