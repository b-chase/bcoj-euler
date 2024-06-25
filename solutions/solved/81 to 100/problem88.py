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
from multiprocessing import freeze_support
from time import perf_counter_ns
from collections import defaultdict


def k_from_factor_product(product, factors):
    n = product - sum(factors)  # number of 1s
    return n + len(factors)




def iter_factors(factors:list[int]=[2,2], product:int=None, max_product:int=24, extendable=False) -> dict[int,set[int]]:
    factor_count = len(factors)
    
    if product is None:
        product = prod(factors)
    if product > max_product:
        return {}
    
    res = defaultdict(lambda: set())
    res[1] = set([2])
    
    x = factors[0]
    rem_terms = factors[1:]
    sub_product = product // x
    max_x = max_product // sub_product
    # print(factors, sub_product, max_x)
    for p_x in range(x, max_x+1):
        # increment first term until too large, and get sublists that are allowed with it
        if len(rem_terms) > 1:
            max_sub_product = min(p_x**len(rem_terms), max_product // p_x)
            sub_iterations = iter_factors(factors[1:], sub_product, max_sub_product)
            for k, m_set in sub_iterations.items():
                res[k].update(m_set)
                for m in m_set:
                    m_new = m*p_x
                    k_new = k + m_new - m - p_x + 1
                    res[k_new].add(m_new)
        elif len(rem_terms) == 1:
            for r in range(rem_terms[0], max_product//p_x + 1):
                m_new = r*p_x
                k_new = k_from_factor_product(m_new, [p_x, r])
                res[k_new].add(m_new)
            
    
    if extendable:
        extended_gen = iter_factors([*factors, 2], product*2, max_product, True)
        for k, m_set in extended_gen.items():
            res[k].update(m_set)
            
    return res
            
        
    



def solve(debug=False):
    
    max_k = 12000
    
    if not debug:
        # this works so much faster
        max_m = max_k*2
        
        factor_lists = iter_factors(max_product=max_m, extendable=True)
        
        min_m_for_k = [(k,min(set_m)) for k, set_m in factor_lists.items()]
        min_m_for_k.sort(key=lambda x: x[0])
        
        # for k,m in min_m_for_k:
        #     print(f"k={k}: M={m}")
        # res.sort(key=lambda x: min(x[1]))
        
        res = sum(set(x[1] for x in min_m_for_k if x[0] <= max_k and x[0]>=2))
        
        print(f'*** Answer: {res} ***')
        return
    
    
    def min_mult(mult_target:int, sum_target:int, term_ct:int) -> list[int]:
        # terms will have product of mult-target and sum of sum-target
        # arg_tuple = (mult_target, sum_target, term_ct)
        # past_result = saved.get(arg_tuple)
        # if past_result is not None:
        #     return past_result
            
        max_term_mult = int(mult_target // (2**(term_ct-1)))  # lowest other terms can be is '2'
        max_term_sum = sum_target - 2*(term_ct-1)  # lowest other terms can be is '2'
        max_term = min(max_term_mult, max_term_sum)
        if term_ct==1:
            if mult_target==sum_target:
                # saved[arg_tuple] = [mult_target]
                return [mult_target]
            else:
                # saved[arg_tuple] = False
                return False
        # print((mult_target, sum_target), term_ct, f'max_term={max_term}')
        
        if mult_target % 2 == 1:
            factor_range = range(3, max_term+1, 2)
        else:
            factor_range = range(2, max_term+1, 2)
            
        for x in factor_range:
            if mult_target % x == 0:
                x_res = min_mult(mult_target//x, sum_target-x, term_ct-1)
                if x_res:
                    # saved[arg_tuple] = [x, *x_res]
                    return [x, *x_res]
        
        # saved[arg_tuple] = False
    
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
    
    
    min_vals_set = set()

    # min_ratio = float('Inf')
    # for k in tqdm(range(2, max_k+1), desc='checking nums', total=max_k-1):
    for k in range(2,max_k+1):
        min_sumprod_num, term_desc = min_product_sum_num(k)
        # print(term_desc)
        # ratio = min_sumprod_num / k
        # if ratio < min_ratio:
        #     min_ratio = ratio
        #     print(f"({ratio:.4f}) {term_desc}")
        min_vals_set.add(min_sumprod_num)
        # print(term_desc)
    # print()
    
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