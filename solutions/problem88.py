# https://projecteuler.net/problem=88
"""<p>A natural number, $N$, that can be written as the sum and product of a given set of at least two natural numbers, $\{a_1, a_2, \dots, a_k\}$ is called a product-sum number: $N = a_1 + a_2 + \cdots + a_k = a_1 \times a_2 \times \cdots \times a_k$.</p>
<p>For example, $6 = 1 + 2 + 3 = 1 \times 2 \times 3$.</p>
<p>For a given set of size, $k$, we shall call the smallest $N$ with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, $k = 2, 3, 4, 5$, and $6$ are as follows.</p>
<ul style="list-style-type:none;">
<li>$k=2$: $4 = 2 \times 2 = 2 + 2$</li>
<li>$k=3$: $6 = 1 \times 2 \times 3 = 1 + 2 + 3$</li>
<li>$k=4$: $8 = 1 \times 1 \times 2 \times 4 = 1 + 1 + 2 + 4$</li>
<li>$k=5$: $8 = 1 \times 1 \times 2 \times 2 \times 2 = 1 + 1 + 2 + 2 + 2$</li><li>$k=6$: $12 = 1 \times 1 \times 1 \times 1 \times 2 \times 6 = 1 + 1 + 1 + 1 + 2 + 6$</li></ul>
<p>Hence for $2 \le k \le 6$, the sum of all the minimal product-sum numbers is $4+6+8+12 = 30$; note that $8$ is only counted once in the sum.</p>
<p>In fact, as the complete set of minimal product-sum numbers for $2 \le k \le 12$ is $\{4, 6, 8, 12, 15, 16\}$, the sum is $61$.</p>
<p>What is the sum of all the minimal product-sum numbers for $2 \le k \le 12000$?</p>

"""

import euler_math as em
from math import prod, factorial
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter_ns

def solve(debug=False):
    
    res=None
    
    def min_mult(mult_target:int, sum_target:int, term_ct:int) -> list[int]:
        # terms will have product of mult-target and sum of sum-target
        max_term_mult = int(mult_target // (2**(term_ct-1)))  # lowest other terms can be is '2'
        max_term_sum = sum_target - 2*(term_ct-1)  # lowest other terms can be is '2'
        max_term = min(max_term_mult, max_term_sum)
        if term_ct==1:
            if mult_target==sum_target:
                return [mult_target]
            else:
                return None
        # print((mult_target, sum_target), term_ct, f'max_term={max_term}')
        if mult_target % 2 == 1:
            factor_range = range(3, max_term+1, 2)
        else:
            factor_range = range(2, max_term+1, 2)
            
        for x in factor_range:
            if mult_target % x == 0:
                x_res = min_mult(mult_target//x, sum_target-x, term_ct-1)
                if x_res:
                    return [x, *x_res]
    
    def min_product_sum_num(k):
        start = perf_counter_ns()
        total = k+1  # target value, will keep incrementing until we hit it
        terms = None
        break_limit = 2*k+1
        while terms is None:
            total += 1
            for q in range(1, k+1):
            # for n in range(0,k-1):
                # n === count of '1's
                # q = k - n
                n = k - q
                # q === remaining terms that are not '1'            
                rem_terms = min_mult(total, total-n, q)
                if rem_terms:
                    # all_terms = [1]*n + rem_terms
                    # assert total == sum(rem_terms) + n, [f'k={k} total={total}', [1]*n + rem_terms]
                    # assert total == em.product(rem_terms)
                    # terms = [1]*n + rem_terms
                    elapsed = (perf_counter_ns() - start)//1000 / 1000
                    return total, f"k={k}: M={total} = {n}*[1] + {rem_terms} in {elapsed:.2f} ms"
            
            if total > break_limit:
                raise Exception(f'Reached breaking limit for k={k}  ({total}>{break_limit})')
    
    max_k = 500
    
    min_vals_set = set()

    min_ratio = float('Inf')
    # for k in tqdm(range(2, max_k+1), desc='checking nums', total=max_k-1):
    for k in range(2,max_k+1):
        min_sumprod_num, term_desc = min_product_sum_num(k)
        # print(term_desc)
        # ratio = min_sumprod_num / k
        # if ratio < min_ratio:
        #     min_ratio = ratio
        #     print(f"({ratio:.4f}) {term_desc}")
        min_vals_set.add(min_sumprod_num)
        print(term_desc)
    print()
    
    # with ThreadPoolExecutor() as executor:
    #     futures = []
    #     for k in range(2, max_k+1):
    #     # for k in range(2,max_k+1):
    #         futures.append(executor.submit(min_product_sum_num, k))
        
    #     # for future in tqdm(as_completed(futures), 'finished', max_k-1):
    #     for future in as_completed(futures):
    #         min_sum_prod_total, term_desc = future.result()
    #         min_vals_set.add(min_sum_prod_total) 
    #         # print(term_desc)
    
    res = sum(min_vals_set)
    
    print(f'*** Answer: {res} ***')