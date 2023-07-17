# https://projecteuler.net/problem=61
"""<p>Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:</p>
</tr></table><p>The ordered set of three $4$-digit numbers: $8128$, $2882$, $8281$, has three interesting properties.</p>
<ol><li>The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).</li>
<li>Each polygonal type: triangle ($P_{3,127}=8128$), square ($P_{4,91}=8281$), and pentagonal ($P_{5,44}=2882$), is represented by a different number in the set.</li>
<li>This is the only set of $4$-digit numbers with this property.</li>
</ol><p>Find the sum of the only ordered set of six cyclic $4$-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.</p>

"""

import euler_math as em

def fig_nums(n_type, max_num=10_000) -> list[int]:
    
    def diff_rule(x):
        return x + n_type-2
    diff = 1
    n = 0
    output = []
    while n < max_num:
        n += diff
        output.append(n)
        diff = diff_rule(diff)
        
    
    return output

def solve(debug=False):
    all_figs = set()
    fig_nums_types = {}

    max_pn = 8
    
    for i in range(3,max_pn+1):
        figs = fig_nums(i, 10000) 
        for fn in figs:
            if fn % 100 >= 10 and fn >= 1000 and fn < 10000:
                fig_nums_types[fn] = i
                all_figs.add(fn)
    
    def matching_rule(num1, num2):
        return num1//100 == num2 % 100
    
    max_seq_len = max_pn-2
    
    def find_next_matches(fig_chains: list[list[int]]):
        new_chains = []

        for try_chain in fig_chains:
            last_num = try_chain[-1]
            seen_types = set(fig_nums_types[fn] for fn in try_chain)

            for fn in all_figs:
                if fig_nums_types[fn] not in seen_types and matching_rule(fn, last_num):
                    if len(try_chain) < max_seq_len-1 or matching_rule(try_chain[0], fn):
                        new_chains.append(try_chain + [fn])
        
        if len(new_chains) == 0:
            return []
        elif len(new_chains[0]) == max_seq_len:
            return new_chains
        else:
            nc_tmp = find_next_matches(new_chains)
            if len(nc_tmp) == 0:
                return []
            else:
                return nc_tmp

    
    res = find_next_matches([[x] for x in all_figs if fig_nums_types[x] == 3])
    

    if debug:
        res.sort(key=lambda x: x[0])
        for r in res:
            print(', '.join(f"{x} ({fig_nums_types[x]})" for x in r))
    res = [(x, sum(x)) for x in res]

    print(f"*** Answer: {res} ***")